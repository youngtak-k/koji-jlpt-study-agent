# Koji — JLPT Study Agent

Læs op til JLPT N5–N1 med din egen lærebog på dit eget sprog. Få hjælp til et svært spørgsmål, vælg opgaver, der passer til i dag, og fortsæt, hvor du slap.

## Begynd med et spørgsmål

**I en eksisterende AI-chat:** upload eller indsæt [Koji-vejledningen](../agent/COACH.md), og send derefter dit spørgsmål. Medtag den relevante sætning, svarmulighederne og dit eget svar, når det er nødvendigt. Brug et kort uddrag eller et tydeligt foto, som din chat kan behandle.

> Følg denne Koji-vejledning. Forklar på dansk. Jeg valgte B, men facit siger C. Her er teksten og min begrundelse. Hvorfor passer C bedre?

**I Codex eller Claude Code med filadgang:** [download dette repository](https://github.com/youngtak-k/koji-jlpt-study-agent/archive/refs/heads/main.zip), pak det ud, og åbn mappen. Skriv:

> Læs AGENTS.md, og hjælp mig med at studere med Koji. Forklar på dansk, og skriv mine noter på dansk. Her er mit spørgsmål fra lærebogen.

Du kan skrive begge instruktioner på dit eget sprog. Du behøver hverken en Koji-server, en separat app, installation af Python eller en API-nøgle til projektet. Du skal have adgang til en AI-assistent, der kan læse vejledningen; dens begrænsninger og omkostninger gælder stadig.

## Eller vælg dagens opgaver

Fortæl Koji, hvilket afsnit af bogen du har åbent, og hvor meget tid du har. Tilføj dit JLPT-målniveau, hvis det ikke allerede er kendt.

> Jeg læser op til N3. Jeg er i begyndelsen af dette grammatikafsnit og har 25 minutter. Hjælp mig med at vælge dagens opgaver.

Koji foreslår et startpunkt, et stoppunkt og en tidsfordeling med plads til repetition, spørgsmål og en kort afslutning. Bogens titel alene er ikke nok til at udlede dens sider eller indhold. Du kan begynde med ét afsnit, før du laver en plan for hele prøven.

## Afslut med én besked

> Jeg blev færdig med spørgsmål 1–4 på 18 minutter. Jeg havde brug for et hint til spørgsmål 3. Det næste er spørgsmål 5.

Koji opsummerer det, du faktisk har gjort, det, der stadig er usikkert, og hvor du skal fortsætte. At stille et spørgsmål tæller ikke automatisk som en fejl; et svar med et hint holdes adskilt fra et selvstændigt svar.

Når filadgangen fungerer, gemmer og kontrollerer Koji din aktuelle oversigt i `local/CURRENT.md` med supplerende noter fra studiesessionerne. I en almindelig chat får du en kort, opdateret studienote, som du selv skal gemme. En genereret note er ikke automatisk gemt lokalt.

## Vend tilbage og fortsæt

> Fortsæt. Jeg har 15 minutter i dag.

Behold den samme studiemappe, eller giv den nye chat din senest gemte note. Koji bruger relevante tidligere resultater til at foreslå en kort repetition og den næste opgave i bogen. En forskel, du forstod med et hint, kan for eksempel få en kort, selvstændig kontrol, før du går videre.

Fortæl det, hvis du har holdt pause:

> Jeg har sprunget en uge over. Jeg har 10 minutter i dag.

Koji tager udgangspunkt i bekræftede fremskridt og reducerer opgaven, så den passer til tiden. Forsømte dage bliver ikke til ekstra timers obligatorisk indhentning. Du kan også bede om en ugentlig gennemgang, rette en note, eksportere din aktuelle note eller sige ”gem ikke denne session”.

## Dine noter vokser med dine studier

Vejledningen er startkulturen; dine studier leverer materialet. Nyttige forklaringer, der vender tilbage, kan blive til forbundne videnssider, adskilt fra dokumentation for, hvad du kan svare på. Du behøver ikke selv at organisere mapper eller føre en ekstra notesbog.

Dine studiefiler ligger under `local/`, som som standard er udeladt fra Git. Behold denne mappe, når du opdaterer Koji: udskift de fælles vejledningsfiler, ikke dine læringsdata. Lokal lagring betyder ikke, at AI-behandlingen foregår offline. Koji arbejder under dine samtaler uden baggrundspåmindelser eller automatisk synkronisering mellem kopier.

Forklaringer og noter følger dine sprogpræferencer med japanske eksempler og læsninger af kanji. Vejledningen er skrevet på engelsk. README-oversættelserne er skrevet af AI og har ikke gennemgået en uafhængig kontrol af modersmålstalende; engelsk er referenceudgaven.

## README-sprog

[Engelsk referenceudgave](../README.md) · [Alle README-sprog](../README.md#readme-languages)

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
