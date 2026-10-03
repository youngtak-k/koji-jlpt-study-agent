# Koji — JLPT Study Agent

Připravujte se na JLPT N5–N1 s vlastní učebnicí a ve vlastním jazyce. Získejte pomoc s obtížnou otázkou, vyberte si práci podle dnešních možností a pokračujte tam, kde jste skončili.

## Začněte otázkou

**Ve stávajícím chatu s AI:** nahrajte nebo vložte [průvodce Koji](../agent/COACH.md) a potom pošlete otázku. Podle potřeby přidejte příslušnou větu, možnosti odpovědí a svou odpověď. Použijte krátký úryvek nebo čitelnou fotografii, kterou váš chat dokáže zpracovat.

> Řiď se tímto průvodcem Koji. Vysvětluj česky. Moje odpověď byla B, ale klíč uvádí C. Tady je text a moje úvaha. Proč se C hodí lépe?

**V Codex nebo Claude Code s přístupem k souborům:** [stáhněte tento repozitář](https://github.com/youngtak-k/koji-jlpt-study-agent/archive/refs/heads/main.zip), rozbalte ho a otevřete složku. Napište:

> Přečti AGENTS.md a pomoz mi studovat s Koji. Vysvětluj česky a piš mé poznámky česky. Tady je moje otázka z učebnice.

Oba pokyny můžete napsat ve vlastním jazyce. Nepotřebujete server Koji, samostatnou aplikaci, instalaci Pythonu ani API klíč pro projekt. Potřebujete přístup k AI asistentovi, který dokáže přečíst průvodce; jeho limity a poplatky nadále platí.

## Nebo vyberte dnešní práci

Řekněte Koji, kterou část učebnice máte otevřenou a kolik máte času. Pokud ještě není známá vaše cílová úroveň JLPT, doplňte ji.

> Připravuji se na N3. Jsem na začátku této gramatické části a mám 25 minut. Pomoz mi vybrat dnešní práci.

Koji navrhne začátek, místo ukončení a časový rozpočet včetně opakování, otázek a krátkého shrnutí. Samotný název knihy nestačí k odvození jejích stran nebo obsahu. Můžete začít jednou částí ještě před vytvořením plánu na celou zkoušku.

## Dokončete jednou zprávou

> Otázky 1–4 jsou hotové; zabraly 18 minut. U otázky 3 byla potřeba nápověda. Další je otázka 5.

Koji shrne, co jste skutečně udělali, co zůstává nejisté a kde pokračovat. Položení otázky se automaticky nepočítá jako chyba; odpověď s nápovědou zůstává oddělená od samostatné odpovědi.

Při funkčním přístupu k souborům Koji uloží a zkontroluje váš aktuální záznam v `local/CURRENT.md` spolu s podpůrnými poznámkami ze studijních sezení. V běžném chatu vám poskytne stručnou aktualizovanou studijní poznámku, kterou si uložíte sami. Vytvoření poznámky neznamená automatické místní uložení.

## Vraťte se a pokračujte

> Pokračujme. Dnes mám 15 minut.

Používejte stejnou studijní složku nebo do nového chatu vložte nejnovější uloženou poznámku. Koji využije relevantní dřívější výsledky k návrhu krátkého opakování a dalšího úkolu z učebnice. Například rozdíl, který jste pochopili s nápovědou, lze krátce ověřit samostatně, než půjdete dál.

Po přestávce o ní řekněte:

> Týden bylo studium přerušené. Dnes mám 10 minut.

Koji vychází z potvrzeného pokroku a zmenší úkol tak, aby se vešel do času. Vynechané dny se nemění v další hodiny povinného dohánění. Můžete také požádat o týdenní přehled, opravit záznam, exportovat aktuální poznámku nebo říct „neukládej toto sezení“.

## Poznámky rostou spolu s vaším studiem

Průvodce funguje jako kvásek; vaše studium dodává materiál. Užitečná vysvětlení, ke kterým se vracíte, mohou přerůst v propojené znalostní stránky, oddělené od dokladů o tom, na co umíte odpovědět. Nemusíte sami uspořádávat složky ani vést druhý sešit.

Vaše studijní soubory zůstávají v `local/`, který je ve výchozím nastavení vyloučen z Gitu. Při aktualizaci Koji tuto složku zachovejte: nahrazujte společné soubory průvodce, nikoli své studijní záznamy. Místní ukládání neznamená zpracování AI bez internetu. Koji pracuje během vašich rozhovorů, bez připomínek na pozadí a automatické synchronizace mezi kopiemi.

Vysvětlení a poznámky respektují vaše jazykové preference a obsahují japonské příklady i čtení kandži. Průvodce je napsaný anglicky. Překlady README vytvořila AI a neprošly nezávislou kontrolou rodilými mluvčími; referenční je anglická verze.

## Jazyky README

[Anglická referenční verze](../README.md) · [Všechny jazyky README](../README.md#readme-languages)

- [English](../README.md)
- [한국어](README.ko.md)
- [日本語](README.ja.md)
- [Español](README.es.md)
- [Français](README.fr.md)
- [Deutsch](README.de.md)
- [简体中文](README.zh-CN.md)
- [繁體中文](README.zh-TW.md)
- [Português (Brasil)](README.pt-BR.md)
- [Italiano](README.it.md)
- [Русский](README.ru.md)
- [Українська](README.uk.md)
- [Polski](README.pl.md)
- [Nederlands](README.nl.md)
- [Svenska](README.sv.md)
- [Dansk](README.da.md)
- [Norsk (bokmål)](README.no.md)
- [Suomi](README.fi.md)
- [Čeština](README.cs.md)
- [Türkçe](README.tr.md)
- [Bahasa Indonesia](README.id.md)
- [Tiếng Việt](README.vi.md)
- [ไทย](README.th.md)
- [हिन्दी](README.hi.md)
- [বাংলা](README.bn.md)
- [العربية](README.ar.md)
- [فارسی](README.fa.md)
- [עברית](README.he.md)
- [Bahasa Melayu](README.ms.md)
- [Filipino](README.tl.md)
