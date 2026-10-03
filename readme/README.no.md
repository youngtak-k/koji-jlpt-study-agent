# Koji — JLPT Study Agent

Studer til JLPT N5–N1 med din egen lærebok, på ditt eget språk. Få hjelp med et vanskelig spørsmål, velg arbeid som passer i dag, og fortsett der du slapp.

## Begynn med et spørsmål

**I en eksisterende KI-chat:** last opp eller lim inn [Koji-veiledningen](../agent/COACH.md), og send deretter spørsmålet ditt. Ta med den relevante setningen, svaralternativene og ditt eget svar når det trengs. Bruk et kort utdrag eller et tydelig bilde som chatten kan behandle.

> Følg denne Koji-veiledningen. Forklar på norsk bokmål. Jeg valgte B, men fasiten sier C. Her er teksten og begrunnelsen min. Hvorfor passer C bedre?

**I Codex eller Claude Code med filtilgang:** [last ned dette kodelageret](https://github.com/youngtak-k/koji-jlpt-study-agent/archive/refs/heads/main.zip), pakk det ut og åpne mappen. Skriv:

> Les AGENTS.md og hjelp meg å studere med Koji. Forklar på norsk bokmål og skriv notatene mine på norsk bokmål. Her er spørsmålet mitt fra læreboken.

Du kan skrive begge instruksjonene på ditt eget språk. Du trenger ingen Koji-server, separat app, Python-installasjon eller API-nøkkel for prosjektet. Du trenger tilgang til en KI-assistent som kan lese veiledningen; grensene og kostnadene der gjelder fortsatt.

## Eller velg dagens arbeid

Fortell Koji hvilken del av boken du har åpen, og hvor mye tid du har. Legg til JLPT-nivået du sikter mot hvis det ikke allerede er kjent.

> Jeg studerer til N3. Jeg er i starten av denne grammatikkdelen og har 25 minutter. Hjelp meg å velge dagens arbeid.

Koji foreslår et startpunkt, et stoppunkt og en tidsfordeling som omfatter repetisjon, spørsmål og en kort avslutning. Boktittelen alene er ikke nok til å utlede sider eller innhold. Du kan begynne med én del før du lager en plan for hele prøven.

## Avslutt med én melding

> Jeg ble ferdig med spørsmål 1–4 på 18 minutter. Jeg trengte et hint til spørsmål 3. Neste er spørsmål 5.

Koji oppsummerer det du faktisk gjorde, det som fortsatt er usikkert, og hvor du skal fortsette. Å stille et spørsmål teller ikke automatisk som en feil; et svar med hint holdes atskilt fra et selvstendig svar.

Når filtilgangen fungerer, lagrer og kontrollerer Koji den gjeldende oversikten din i `local/CURRENT.md`, med støttende notater fra studieøktene. I en vanlig chat får du et kort, oppdatert studienotat som du må lagre selv. Et generert notat er ikke automatisk lagret lokalt.

## Kom tilbake og fortsett

> Fortsett. Jeg har 15 minutter i dag.

Behold den samme studiemappen, eller legg ved det sist lagrede notatet i den nye chatten. Koji bruker relevante tidligere resultater til å foreslå en kort repetisjon og neste oppgave i boken. En forskjell du forsto med et hint, kan for eksempel følges opp med en kort selvstendig sjekk før du går videre.

Si fra hvis du har hatt en pause:

> Jeg har gått glipp av en uke. Jeg har 10 minutter i dag.

Koji tar utgangspunkt i bekreftet fremgang og reduserer oppgaven så den passer til tiden. Tapte dager blir ikke til ekstra timer med obligatorisk innhenting. Du kan også be om en ukentlig gjennomgang, rette et notat, eksportere det gjeldende notatet eller si «ikke lagre denne økten».

## Notatene vokser med studiene dine

Veiledningen er startkulturen; studiene dine gir materialet. Nyttige forklaringer som går igjen, kan bli til sammenkoblede kunnskapssider, atskilt fra dokumentasjon på hva du kan svare på. Du trenger ikke å organisere mapper eller føre en ekstra notatbok selv.

Studiefilene dine ligger under `local/`, som er utelatt fra Git som standard. Behold denne mappen når du oppdaterer Koji: erstatt de felles veiledningsfilene, ikke læringsdataene dine. Lokal lagring betyr ikke at KI-behandlingen skjer uten nettilkobling. Koji arbeider under samtalene dine, uten bakgrunnspåminnelser eller automatisk synkronisering mellom kopier.

Forklaringer og notater følger språkpreferansene dine, med japanske eksempler og lesemåter for kanji. Veiledningen er skrevet på engelsk. README-oversettelsene er skrevet av KI og har ikke blitt uavhengig vurdert av morsmålsbrukere; engelsk er referanseutgaven.

## README-språk

[Engelsk referanseutgave](../README.md) · [Alle README-språk](../README.md#readme-languages)

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
