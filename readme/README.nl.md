# Koji — JLPT Study Agent

Studeer voor JLPT N5–N1 met je eigen studieboek, in je eigen taal. Krijg hulp bij een moeilijke vraag, kies werk dat vandaag past en ga verder waar je gebleven was.

## Begin met een vraag

**In een bestaande AI-chat:** upload of plak de [Koji-handleiding](../agent/COACH.md) en stuur daarna je vraag. Voeg waar nodig de relevante zin, antwoordopties en je eigen antwoord toe. Gebruik een kort fragment of een leesbare foto die je chat kan verwerken.

> Volg deze Koji-handleiding. Geef uitleg in het Nederlands. Ik koos B, maar volgens het antwoordmodel is C juist. Hier zijn de tekst en mijn redenering. Waarom past C beter?

**In Codex of Claude Code met bestandstoegang:** [download deze repository](https://github.com/youngtak-k/koji-jlpt-study-agent/archive/refs/heads/main.zip), pak het bestand uit en open de map. Vraag:

> Lees AGENTS.md en help me studeren met Koji. Geef uitleg in het Nederlands en houd mijn notities in het Nederlands bij. Hier is mijn vraag uit het studieboek.

Je kunt beide prompts in je eigen taal schrijven. Je hebt geen Koji-server, aparte app, Python-installatie of API-sleutel voor het project nodig. Wel heb je toegang nodig tot een AI-assistent die de handleiding kan lezen; de limieten en kosten daarvan blijven gelden.

## Of kies het werk voor vandaag

Vertel Koji welk onderdeel van je studieboek je open hebt en hoeveel tijd je hebt. Geef ook je beoogde JLPT-niveau als dat nog niet bekend is.

> Ik studeer voor N3. Ik sta aan het begin van dit grammaticaonderdeel en heb 25 minuten. Help me het werk voor vandaag te kiezen.

Koji stelt een beginpunt, een stoppunt en een tijdsindeling voor, inclusief herhaling, vragen en een korte afronding. Alleen de titel van een boek is niet genoeg om de pagina’s of inhoud ervan af te leiden. Je kunt met één onderdeel beginnen voordat je een plan voor het hele examen maakt.

## Rond af met één bericht

> Ik heb vragen 1–4 in 18 minuten afgerond. Bij vraag 3 had ik een hint nodig. Vraag 5 is de volgende.

Koji vat samen wat je daadwerkelijk hebt gedaan, wat nog onzeker is en waar je verdergaat. Een vraag stellen telt niet automatisch als een fout; een antwoord met een hint blijft onderscheiden van een zelfstandig antwoord.

Met werkende bestandstoegang slaat Koji je actuele overzicht op in `local/CURRENT.md` en controleert het, met ondersteunende sessienotities. In een gewone chat krijg je een compacte, bijgewerkte studienotitie die je zelf moet opslaan. Een gegenereerde notitie wordt niet automatisch lokaal opgeslagen.

## Kom terug en ga verder

> Ga verder. Ik heb vandaag 15 minuten.

Gebruik dezelfde studiemap of geef in de nieuwe chat je laatst opgeslagen notitie mee. Koji gebruikt relevante eerdere resultaten om een korte herhaling en de volgende opdracht in je boek voor te stellen. Een onderscheid dat je met een hint begreep, kan bijvoorbeeld kort zelfstandig worden getoetst voordat je verdergaat.

Vertel het als je een pauze hebt genomen:

> Ik heb een week niet gestudeerd. Ik heb vandaag 10 minuten.

Koji gaat uit van bevestigde voortgang en verkleint de opdracht zodat die past. Gemiste dagen worden geen extra uren verplicht inhaalwerk. Je kunt ook om een weekoverzicht vragen, een notitie corrigeren, je actuele notitie exporteren of zeggen: ‘sla deze sessie niet op’.

## Je notities groeien met je studie mee

De handleiding is de startercultuur; jouw studie levert het materiaal. Nuttige uitleg die vaker terugkomt, kan uitgroeien tot gekoppelde kennispagina’s, los van het bewijs van wat je kunt beantwoorden. Je hoeft niet zelf mappen te ordenen of een tweede notitieboek bij te houden.

Je studiebestanden blijven onder `local/`, dat standaard van Git is uitgesloten. Bewaar deze map als je Koji bijwerkt: vervang de gedeelde handleidingsbestanden, niet je leergegevens. Lokale opslag betekent niet dat de AI offline werkt. Koji werkt tijdens je gesprekken, zonder herinneringen op de achtergrond of automatische synchronisatie tussen kopieën.

Uitleg en notities volgen je taalvoorkeuren, met Japanse voorbeelden en leeswijzen van kanji. De handleiding is in het Engels geschreven. De README-vertalingen zijn door AI gemaakt en niet onafhankelijk gecontroleerd door moedertaalsprekers; Engels is de referentieversie.

## README-talen

[Engelse referentieversie](../README.md) · [Alle README-talen](../README.md#readme-languages)

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
