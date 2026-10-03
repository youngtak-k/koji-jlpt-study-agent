# Koji — JLPT Study Agent

Maghanda para sa JLPT N5–N1 gamit ang sarili mong aklat at wika. Magpatulong sa mahirap na tanong, pumili ng gawaing kasya sa oras ngayon, at magpatuloy kung saan ka huminto.

## Magsimula sa isang tanong

**Sa AI chat na ginagamit mo na:** i-upload o i-paste ang [gabay ng Koji](../agent/COACH.md), saka ipadala ang tanong. Isama ang kaugnay na pangungusap, mga pagpipilian at sagot mo kung kailangan. Gumamit ng maikling sipi o malinaw na larawang kayang basahin ng chat.

> Sundin ang gabay ng Koji na ito. Magpaliwanag sa Filipino. B ang pinili ko, pero C ang nasa susi sa pagwawasto. Narito ang teksto at paliwanag ng sagot ko. Bakit mas angkop ang C?

**Sa Codex o Claude Code na may access sa mga file:** [i-download ang repository na ito](https://github.com/youngtak-k/koji-jlpt-study-agent/archive/refs/heads/main.zip), i-unzip at buksan ang folder. Sabihin:

> Basahin ang AGENTS.md at tulungan akong mag-aral sa Koji. Magpaliwanag at isulat ang mga tala ko sa Filipino. Narito ang tanong ko mula sa aklat.

Maaari mong isulat ang alinmang kahilingan sa sarili mong wika. Hindi kailangan ng Koji server, hiwalay na app, pag-install ng Python o API key ng proyekto. Kailangan mo ng access sa AI assistant na makababasa ng gabay; naaangkop pa rin ang mga limitasyon at bayarin nito.

## O piliin ang aaralin ngayon

Sabihin sa Koji kung aling bahagi ng aklat ang nakabukas at gaano karaming oras ang mayroon ka. Idagdag ang target mong antas ng JLPT kung hindi pa ito alam.

> Naghahanda ako para sa N3. Nasa simula ako ng bahaging ito ng gramatika at may 25 minuto. Tulungan akong piliin ang aaralin ngayon.

Nagmumungkahi ang Koji ng simula, hihintuan at hatian ng oras na may pagbabalik-aral, mga tanong at maikling pagtatapos. Hindi sapat ang pamagat ng aklat para malaman ang mga pahina o nilalaman nito. Maaari kang magsimula sa isang bahagi bago magplano para sa buong pagsusulit.

## Tapusin sa isang mensahe

> Natapos ko ang mga tanong 1–4 sa loob ng 18 minuto. Nangailangan ako ng pahiwatig sa tanong 3. Susunod ang tanong 5.

Ibinubuod ng Koji ang talagang nagawa mo, ang hindi pa tiyak at kung saan magpapatuloy. Hindi awtomatikong mali ang sagot dahil nagtanong ka; hiwalay ang sagot na may pahiwatig sa sagot na nagawa mong mag-isa.

Kapag gumagana ang access sa file, sine-save at sinusuri ng Koji ang kasalukuyang rekord mo sa `local/CURRENT.md`, kasama ang mga pantulong na tala ng sesyon. Sa karaniwang chat, nagbibigay ito ng maikli at na-update na tala sa pag-aaral na ikaw mismo ang magse-save. Ang paggawa ng tala ay hindi awtomatikong pag-save sa iyong device.

## Bumalik at magpatuloy

> Ituloy natin. May 15 minuto ako ngayon.

Panatilihin ang parehong folder ng pag-aaral, o ibigay sa bagong chat ang pinakahuling talang na-save mo. Gumagamit ang Koji ng kaugnay na naunang ebidensya para magmungkahi ng maikling pagbabalik-aral at susunod na gawain sa aklat. Halimbawa, bago magpatuloy, maaaring maikling suriin nang walang tulong ang pagkakaibang naunawaan mo noon sa pamamagitan ng pahiwatig.

Pagkatapos ng pahinga, sabihin ito:

> Hindi ako nakapag-aral nang isang linggo. May 10 minuto ako ngayon.

Nagsisimula ang Koji sa nakumpirmang progreso at pinapaliit ang gawain para magkasya sa oras. Ang mga araw na nalaktawan ay hindi nagiging dagdag na oras ng sapilitang paghahabol. Maaari ka ring humiling ng lingguhang pagrepaso, magwasto ng rekord, i-export ang kasalukuyang tala o magsabi ng “huwag i-save ang sesyong ito”.

## Lumalago ang mga tala kasabay ng pag-aaral

Ang gabay ang panimulang pampaalsa; ang pag-aaral mo ang nagbibigay ng materyal. Ang kapaki-pakinabang na mga paliwanag na nauulit ay maaaring maging magkakaugnay na pahina ng kaalaman, hiwalay sa ebidensya ng kaya mong sagutin. Hindi mo kailangang mag-ayos ng mga folder o magpanatili ng pangalawang kuwaderno.

Nananatili ang mga file ng pag-aaral sa `local/`, na hindi kasama sa Git bilang default. Itabi ang folder na ito kapag nag-a-update ng Koji; palitan ang mga shared guide file, hindi ang mga rekord ng pag-aaral mo. Ang lokal na pag-iimbak ay hindi nangangahulugang offline ang pagproseso ng AI. Gumagana ang Koji sa panahon ng pag-uusap, walang background reminder o awtomatikong pag-sync sa pagitan ng mga kopya.

Sinusunod ng mga paliwanag at tala ang pinili mong wika, kasama ang mga halimbawang Hapon at pagbasa ng kanji. Nakasulat sa Ingles ang gabay. AI ang gumawa ng mga salin ng README at wala pang hiwalay na pagsusuri ng katutubong tagapagsalita; ang edisyong Ingles ang sanggunian.

## Mga wika ng README

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
