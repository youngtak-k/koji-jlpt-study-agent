# Koji — JLPT Study Agent

Study for JLPT N5–N1 with your own textbook, in your own language. Get help with a difficult question, choose work that fits today, and pick up where you left off.

## Start with a question

**In an existing AI chat:** upload or paste the [Koji guide](agent/COACH.md), then send your question. Include the relevant sentence, choices, and your answer when needed. Use a short excerpt or a readable photo your chat can process.

> Follow this Koji guide. Explain in English. I chose B, but the answer key says C. Here is the passage and my reasoning. Why is C better?

**In Codex or Claude Code with file access:** [download this repository](https://github.com/youngtak-k/koji-jlpt-study-agent/archive/refs/heads/main.zip), unzip it, and open the folder. Ask:

> Read AGENTS.md and help me study with Koji. Explain in English and keep my notes in English. Here is my textbook question.

You can write either prompt in your own language. No Koji server, separate app, Python installation, or project API key is needed. You need access to an AI assistant that can read the guide; its limits and costs still apply.

## Or choose today's work

Tell Koji which book section is open and how much time you have. Add your target JLPT level if it is not already known.

> I'm studying for N3. I'm at the start of this grammar section and have 25 minutes. Help me choose today's work.

Koji proposes a starting point, a stopping point, and a time budget including review, questions, and a short wrap-up. A book title alone is not enough to infer its pages or contents. You can start with one section before making a whole-exam plan.

## Finish in one message

> I finished questions 1–4 in 18 minutes. I needed a hint for question 3. Next is question 5.

Koji summarizes what you actually did, what remains uncertain, and where to resume. Asking a question does not automatically count as an error; a hinted answer stays distinct from an independent one.

With working file access, Koji saves and checks your current record at `local/CURRENT.md`, with supporting session notes. In an ordinary chat, it gives you a compact updated study note to save yourself. A generated note is not an automatic local save.

## Come back and continue

> Continue. I have 15 minutes today.

Keep the same study folder, or supply your latest saved note in the new chat. Koji uses relevant earlier evidence to suggest a small review and the next book task. For example, a distinction you resolved with a hint can get a brief independent check before you move on.

After a break, say so:

> I missed a week. I have 10 minutes today.

Koji starts from confirmed progress and reduces the task to fit. Missed days do not turn into extra hours of compulsory catch-up. You can also ask for a weekly review, correct a record, export your current note, or say “don't save this session.”

## Your notes grow with your study

The guide is the starter culture; your study supplies the material. Useful recurring explanations can become linked knowledge pages, separate from evidence of what you can answer. You do not need to organize folders or maintain a second notebook yourself.

Your study files stay under `local/`, excluded from Git by default. Keep this folder when updating Koji; replace the shared guide files, not your learning records. Local storage does not mean offline AI processing. Koji works during your conversations, without background reminders or automatic synchronization between copies.

Explanations and notes follow your language preferences, with Japanese examples and kanji readings. The guide is written in English. README translations are AI-authored and have not had independent native-speaker review; English is the reference edition.

## README languages

- [English](README.md)
- [한국어](readme/README.ko.md)
- [日本語](readme/README.ja.md)
- [Español](readme/README.es.md)
- [Français](readme/README.fr.md)
- [Deutsch](readme/README.de.md)
- [简体中文](readme/README.zh-CN.md)
- [繁體中文](readme/README.zh-TW.md)
- [Português (Brasil)](readme/README.pt-BR.md)
- [Italiano](readme/README.it.md)
- [Русский](readme/README.ru.md)
- [Українська](readme/README.uk.md)
- [Polski](readme/README.pl.md)
- [Nederlands](readme/README.nl.md)
- [Svenska](readme/README.sv.md)
- [Dansk](readme/README.da.md)
- [Norsk (bokmål)](readme/README.no.md)
- [Suomi](readme/README.fi.md)
- [Čeština](readme/README.cs.md)
- [Türkçe](readme/README.tr.md)
- [Bahasa Indonesia](readme/README.id.md)
- [Tiếng Việt](readme/README.vi.md)
- [ไทย](readme/README.th.md)
- [हिन्दी](readme/README.hi.md)
- [বাংলা](readme/README.bn.md)
- [العربية](readme/README.ar.md)
- [فارسی](readme/README.fa.md)
- [עברית](readme/README.he.md)
- [Bahasa Melayu](readme/README.ms.md)
- [Filipino](readme/README.tl.md)
