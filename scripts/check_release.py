"""Check the distributable Koji files. Python is only needed for maintenance."""

from __future__ import annotations

import argparse
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit


LOCALES = "ar bn cs da de es fa fi fr he hi id it ja ko ms nl no pl pt-BR ru sv th tl tr uk vi zh-CN zh-TW".split()
REQUIRED = {
    ".gitignore", "AGENTS.md", "CLAUDE.md", "LICENSE", "README.md", "VERSION",
    "agent/COACH.md", "templates/CURRENT.md", "templates/SESSION.md",
    "templates/CONCEPT.md", "templates/KNOWLEDGE_INDEX.md",
    "scripts/check_release.py", "tests/test_release.py",
} | {f"readme/README.{locale}.md" for locale in LOCALES}
PRODUCT_TEXT = {p for p in REQUIRED if p.endswith(".md")}


def manifest_errors(paths: set[str]) -> list[str]:
    """An explicit file set prevents accidental publication of local state."""
    return [f"Unexpected distributable file: {p}" for p in sorted(paths - REQUIRED)] + [
        f"Missing distributable file: {p}" for p in sorted(REQUIRED - paths)
    ]


def index_matches_worktree(root: Path) -> bool:
    result = subprocess.run(["git", "diff", "--quiet", "--no-ext-diff"], cwd=root)
    if result.returncode not in (0, 1):
        raise RuntimeError("Could not compare the Git index with the working files.")
    return result.returncode == 0


def link_errors(root: Path, source: str, content: str, paths: set[str]) -> list[str]:
    errors = []
    # Examples in fenced code are not live navigation links.
    prose = re.sub(r"```.*?```", "", content, flags=re.S)
    for raw in re.findall(r"\[[^\]\n]+\]\(([^\s)]+)\)", prose):
        url = urlsplit(raw.strip("<>"))
        if url.scheme or url.netloc or not url.path:
            continue
        target = (root / PurePosixPath(source).parent / unquote(url.path)).resolve()
        try:
            relative = target.relative_to(root.resolve()).as_posix()
        except ValueError:
            errors.append(f"Link leaves the package: {source} -> {raw}")
            continue
        if relative not in paths:
            errors.append(f"Link points outside the distribution: {source} -> {raw}")
    return errors


def validate(root: Path, paths: set[str]) -> list[str]:
    errors = manifest_errors(paths)
    for name in sorted(paths & REQUIRED):
        path = root / name
        if path.is_symlink() or not path.is_file():
            errors.append(f"Expected an ordinary file: {name}")
            continue
        content = path.read_text(encoding="utf-8")
        if not content.strip():
            errors.append(f"Empty file: {name}")
        if name in PRODUCT_TEXT:
            errors.extend(link_errors(root, name, content, paths))
            if re.search(r"PRODUCT_REQUIREMENTS|local/product|local/prototypes|/Users/|/home/|koji/engine|docs/research", content):
                errors.append(f"Internal reference in product guidance: {name}")
        if name == "README.md" or name.startswith("readme/"):
            expected = {"README.md"} | {f"readme/README.{x}.md" for x in LOCALES}
            found = set()
            for raw in re.findall(r"\]\(([^\s)]+)\)", content):
                if urlsplit(raw).scheme:
                    continue
                dest = (root / Path(name).parent / raw).resolve()
                try:
                    found.add(dest.relative_to(root.resolve()).as_posix())
                except ValueError:
                    pass
            if not expected <= found:
                errors.append(f"Incomplete language navigation: {name}")
    coach = root / "agent/COACH.md"
    packet = root / "templates/CURRENT.md"
    version = root / "VERSION"
    if coach.is_file() and packet.is_file():
        blocks = re.findall(r"```markdown\n(.*?)\n```", coach.read_text(), re.S)
        if len(blocks) != 1 or blocks[0].strip() != packet.read_text().strip():
            errors.append("The portable packet and workspace template differ.")
    if coach.is_file() and version.is_file():
        if f"Guide version: {version.read_text().strip()}." not in coach.read_text():
            errors.append("The coach guide and package versions differ.")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tracked", action="store_true", help="Check exactly the Git index (use after staging).")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    if args.tracked:
        if not index_matches_worktree(root):
            print("FAIL: tracked files differ from the Git index; stage the intended contents before checking.")
            return 1
        result = subprocess.run(["git", "ls-files", "-z"], cwd=root, check=True, capture_output=True)
        paths = set(result.stdout.decode().strip("\0").split("\0")) - {""}
        # A forced add bypasses ignore rules, so the manifest check is still mandatory.
        for probe in ["local/CURRENT.md", "local/sessions/example.md", "docs/PRODUCT_REQUIREMENTS.md"]:
            ignored = subprocess.run(["git", "check-ignore", "--no-index", "-q", probe], cwd=root)
            if ignored.returncode != 0:
                print(f"FAIL: private path is not ignored: {probe}")
                return 1
    else:
        paths = set()
        for path in root.rglob("*"):
            relative = path.relative_to(root)
            if any(part in {".git", "local", "__pycache__", ".DS_Store"} for part in relative.parts):
                continue
            if path.is_file() or path.is_symlink():
                paths.add(relative.as_posix())
    errors = validate(root, paths)
    if errors:
        print("\n".join(f"FAIL: {error}" for error in errors))
        return 1
    print(f"PASS: {len(paths)} distributable files; private paths excluded; links and 30 README editions checked.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
