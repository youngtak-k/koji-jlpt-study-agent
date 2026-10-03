# Koji — JLPT Study Agent

Opiskele JLPT-tasoja N5–N1 varten omalla oppikirjallasi ja omalla kielelläsi. Saat apua vaikeaan kysymykseen, valitset tähän päivään sopivan tehtävän ja jatkat siitä, mihin jäit.

## Aloita kysymyksellä

**Nykyisessä tekoälykeskustelussa:** lataa tai liitä [Koji-opas](../agent/COACH.md) ja lähetä sitten kysymyksesi. Liitä tarvittaessa asiaankuuluva lause, vastausvaihtoehdot ja oma vastauksesi. Käytä lyhyttä katkelmaa tai selkeää kuvaa, jonka keskustelupalvelusi pystyy käsittelemään.

> Noudata tätä Koji-opasta. Selitä suomeksi. Valitsin B:n, mutta vastausavaimen mukaan oikea vastaus on C. Tässä ovat teksti ja perusteluni. Miksi C sopii paremmin?

**Codex- tai Claude Code -ympäristössä, kun tiedostojen käyttö on mahdollista:** [lataa tämä tietovarasto](https://github.com/youngtak-k/koji-jlpt-study-agent/archive/refs/heads/main.zip), pura se ja avaa kansio. Pyydä:

> Lue AGENTS.md ja auta minua opiskelemaan Kojin avulla. Selitä suomeksi ja kirjoita muistiinpanoni suomeksi. Tässä on kysymykseni oppikirjasta.

Voit kirjoittaa kummankin pyynnön omalla kielelläsi. Et tarvitse Koji-palvelinta, erillistä sovellusta, Python-asennusta tai projektin API-avainta. Tarvitset pääsyn tekoälyavustajaan, joka osaa lukea oppaan; sen käyttörajat ja maksut ovat edelleen voimassa.

## Tai valitse päivän tehtävät

Kerro Kojille, mikä oppikirjan osio on avoinna ja paljonko sinulla on aikaa. Lisää tavoittelemasi JLPT-taso, jos se ei ole vielä tiedossa.

> Opiskelen N3-koetta varten. Olen tämän kielioppiosion alussa, ja minulla on 25 minuuttia. Auta minua valitsemaan päivän tehtävät.

Koji ehdottaa aloituskohtaa, lopetuskohtaa ja ajankäyttöä, joka sisältää kertauksen, kysymykset ja lyhyen yhteenvedon. Pelkkä kirjan nimi ei riitä sen sivujen tai sisällön päättelemiseen. Voit aloittaa yhdestä osiosta ennen koko kokeeseen valmistavan suunnitelman tekemistä.

## Lopeta yhdellä viestillä

> Sain kysymykset 1–4 valmiiksi 18 minuutissa. Tarvitsin vihjeen kysymykseen 3. Seuraavana on kysymys 5.

Koji tekee yhteenvedon siitä, mitä todella teit, mikä on vielä epävarmaa ja mistä jatkat. Kysymyksen esittäminen ei automaattisesti tarkoita virhettä; vihjeen avulla annettu vastaus erotetaan itsenäisestä vastauksesta.

Kun tiedostojen käyttö toimii, Koji tallentaa ja tarkistaa ajantasaisen tietueesi tiedostossa `local/CURRENT.md` sekä sitä tukevat opiskelukertojen muistiinpanot. Tavallisessa keskustelussa saat tiiviin, päivitetyn opiskelumuistiinpanon, joka sinun on tallennettava itse. Muistiinpanon luominen ei tarkoita automaattista paikallista tallennusta.

## Palaa ja jatka

> Jatketaan. Minulla on tänään 15 minuuttia.

Säilytä sama opiskelukansio tai anna uudessa keskustelussa viimeksi tallentamasi muistiinpano. Koji ehdottaa aiempien olennaisten tulosten perusteella lyhyttä kertausta ja seuraavaa oppikirjan tehtävää. Esimerkiksi vihjeen avulla ymmärtämäsi ero voidaan tarkistaa lyhyesti ilman apua ennen kuin jatkat eteenpäin.

Kerro, jos olet pitänyt tauon:

> Minulta jäi viikko väliin. Minulla on tänään 10 minuuttia.

Koji lähtee vahvistetusta edistymisestä ja pienentää tehtävää käytettävissä olevan ajan mukaan. Väliin jääneet päivät eivät muutu ylimääräisiksi tunneiksi pakollista kirimistä. Voit myös pyytää viikkokatsausta, korjata merkinnän, viedä nykyisen muistiinpanosi tai sanoa ”älä tallenna tätä opiskelukertaa”.

## Muistiinpanosi kasvavat opiskelun mukana

Opas toimii juurena, ja opiskelusi tuottaa aineiston. Hyödyllisistä, toistuvista selityksistä voi muodostua toisiinsa linkitettyjä tietosivuja, jotka pidetään erillään näytöstä siitä, mihin osaat vastata. Sinun ei tarvitse itse järjestellä kansioita tai ylläpitää toista muistikirjaa.

Opiskelutiedostosi pysyvät `local/`-kansiossa, joka on oletuksena jätetty Gitin ulkopuolelle. Säilytä tämä kansio Koji-päivityksissä: korvaa yhteiset opastiedostot, älä opiskelutietojasi. Paikallinen tallennus ei tarkoita tekoälykäsittelyä ilman verkkoyhteyttä. Koji toimii keskustelujesi aikana ilman taustamuistutuksia tai kopioiden automaattista synkronointia.

Selitykset ja muistiinpanot noudattavat kielitoiveitasi, ja mukana on japaninkielisiä esimerkkejä sekä kanjien lukutapoja. Opas on kirjoitettu englanniksi. README-käännökset ovat tekoälyn laatimia, eikä riippumaton äidinkielinen tarkastaja ole tarkistanut niitä; englanti on vertailuversio.

## README-kielet

[Englanninkielinen vertailuversio](../README.md) · [Kaikki README-kielet](../README.md#readme-languages)

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
