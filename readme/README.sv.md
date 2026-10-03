# Koji — JLPT Study Agent

Studera inför JLPT N5–N1 med din egen lärobok, på ditt eget språk. Få hjälp med en svår fråga, välj arbete som ryms i dagens tid och fortsätt där du slutade.

## Börja med en fråga

**I en befintlig AI-chatt:** ladda upp eller klistra in [Koji-guiden](../agent/COACH.md) och skicka sedan din fråga. Ta med den relevanta meningen, svarsalternativen och ditt eget svar när det behövs. Använd ett kort utdrag eller ett tydligt foto som chatten kan bearbeta.

> Följ den här Koji-guiden. Förklara på svenska. Jag valde B, men facit säger C. Här är texten och mitt resonemang. Varför passar C bättre?

**I Codex eller Claude Code med filåtkomst:** [ladda ned det här kodarkivet](https://github.com/youngtak-k/koji-jlpt-study-agent/archive/refs/heads/main.zip), packa upp det och öppna mappen. Skriv:

> Läs AGENTS.md och hjälp mig att studera med Koji. Förklara på svenska och skriv mina anteckningar på svenska. Här är min fråga ur läroboken.

Du kan skriva båda uppmaningarna på ditt eget språk. Du behöver ingen Koji-server, separat app, Python-installation eller API-nyckel för projektet. Du behöver tillgång till en AI-assistent som kan läsa guiden; dess begränsningar och kostnader gäller fortfarande.

## Eller välj dagens arbete

Berätta för Koji vilket avsnitt i boken du har öppet och hur mycket tid du har. Ange också din JLPT-målnivå om den inte redan är känd.

> Jag studerar inför N3. Jag är i början av det här grammatikavsnittet och har 25 minuter. Hjälp mig att välja dagens arbete.

Koji föreslår en startpunkt, en slutpunkt och en tidsfördelning som omfattar repetition, frågor och en kort avslutning. Enbart en boktitel räcker inte för att avgöra bokens sidor eller innehåll. Du kan börja med ett avsnitt innan du gör en plan för hela provet.

## Avsluta med ett meddelande

> Jag blev klar med frågorna 1–4 på 18 minuter. Jag behövde en ledtråd till fråga 3. Nästa är fråga 5.

Koji sammanfattar vad du faktiskt gjorde, vad som fortfarande är osäkert och var du ska fortsätta. Att ställa en fråga räknas inte automatiskt som ett fel; ett svar med ledtråd hålls åtskilt från ett självständigt svar.

När filåtkomsten fungerar sparar och kontrollerar Koji din aktuella sammanställning i `local/CURRENT.md`, med stödjande anteckningar från studiepassen. I en vanlig chatt får du en kort, uppdaterad studieanteckning som du själv sparar. En genererad anteckning innebär inte att den automatiskt har sparats lokalt.

## Kom tillbaka och fortsätt

> Fortsätt. Jag har 15 minuter i dag.

Behåll samma studiemapp eller skicka med din senast sparade anteckning i den nya chatten. Koji använder relevanta tidigare resultat för att föreslå en kort repetition och nästa uppgift i boken. En skillnad som du förstod med hjälp av en ledtråd kan till exempel följas upp med en kort självständig kontroll innan du går vidare.

Berätta om du har haft ett uppehåll:

> Jag har missat en vecka. Jag har 10 minuter i dag.

Koji utgår från bekräftade framsteg och minskar uppgiften så att den ryms. Missade dagar blir inte extra timmar av obligatoriskt ikapparbete. Du kan också be om en veckogenomgång, rätta en anteckning, exportera din aktuella anteckning eller säga ”spara inte det här studiepasset”.

## Dina anteckningar växer med dina studier

Guiden är startkulturen; dina studier ger materialet. Användbara förklaringar som återkommer kan bli länkade kunskapssidor, åtskilda från belägg för vad du kan svara på. Du behöver inte själv ordna mappar eller sköta en andra anteckningsbok.

Dina studiefiler ligger under `local/`, som är undantagen från Git som standard. Behåll den här mappen när du uppdaterar Koji: ersätt de gemensamma guidefilerna, inte dina studieanteckningar. Lokal lagring betyder inte att AI-bearbetningen sker offline. Koji arbetar under dina samtal, utan påminnelser i bakgrunden eller automatisk synkronisering mellan kopior.

Förklaringar och anteckningar följer dina språkval, med japanska exempel och läsningar av kanji. Guiden är skriven på engelska. README-översättningarna är AI-skrivna och har inte granskats oberoende av modersmålstalare; engelska är referensutgåvan.

## README-språk

[Engelsk referensutgåva](../README.md) · [Alla README-språk](../README.md#readme-languages)

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
