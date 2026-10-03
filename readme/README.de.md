# Koji — JLPT Study Agent

Lerne für JLPT N5–N1 mit deinem eigenen Lehrbuch und in deiner Sprache. Lass dir bei schwierigen Fragen helfen, wähle Aufgaben passend zur heutigen Zeit und mache dort weiter, wo du aufgehört hast.

## Mit einer Frage beginnen

**In einem bestehenden KI-Chat:** Lade den [Koji-Leitfaden](../agent/COACH.md) hoch oder füge ihn ein und stelle dann deine Frage. Gib bei Bedarf den betreffenden Satz, die Antwortmöglichkeiten und deine Antwort an. Verwende einen kurzen Auszug oder ein gut lesbares Foto, das dein Chat verarbeiten kann.

> Folge diesem Koji-Leitfaden. Erkläre auf Deutsch. Ich habe B gewählt, aber laut Lösung ist C richtig. Hier sind der Text und meine Überlegungen. Warum passt C besser?

**In Codex oder Claude Code mit Dateizugriff:** [Lade dieses Repository herunter](https://github.com/youngtak-k/koji-jlpt-study-agent/archive/refs/heads/main.zip), entpacke es und öffne den Ordner. Bitte dann:

> Lies AGENTS.md und hilf mir, mit Koji zu lernen. Erkläre auf Deutsch und führe meine Notizen auf Deutsch. Hier ist meine Frage aus dem Lehrbuch.

Beide Anfragen kannst du in deiner Sprache formulieren. Du brauchst keinen Koji-Server, keine separate App, keine Python-Installation und keinen projektspezifischen API-Schlüssel. Du benötigst Zugang zu einem KI-Assistenten, der den Leitfaden lesen kann; dessen Nutzungslimits und Kosten gelten weiterhin.

## Oder die heutige Aufgabe auswählen

Sage Koji, welchen Abschnitt im Buch du aufgeschlagen hast und wie viel Zeit du hast. Nenne auch dein JLPT-Zielniveau, falls es noch nicht bekannt ist.

> Ich lerne für N3. Ich bin am Anfang dieses Grammatikabschnitts und habe 25 Minuten. Hilf mir, die heutige Aufgabe auszuwählen.

Koji schlägt Anfang, Ende und ein Zeitbudget einschließlich Wiederholung, Fragen und kurzem Abschluss vor. Der Buchtitel allein reicht nicht aus, um Seiten oder Inhalte abzuleiten. Du kannst mit einem Abschnitt beginnen, bevor du die gesamte Prüfungsvorbereitung planst.

## Mit einer Nachricht abschließen

> Ich habe die Aufgaben 1–4 in 18 Minuten erledigt. Bei Aufgabe 3 brauchte ich einen Hinweis. Als Nächstes kommt Aufgabe 5.

Koji fasst zusammen, was du tatsächlich getan hast, was noch unklar ist und wo es weitergeht. Eine Frage zählt nicht automatisch als Fehler; eine Antwort mit Hinweis bleibt von einer selbstständigen Antwort getrennt.

Bei funktionierendem Dateizugriff speichert und prüft Koji deinen aktuellen Stand in `local/CURRENT.md`, ergänzt durch Sitzungsnotizen. In einem normalen Chat erhältst du eine kompakte, aktualisierte Lernnotiz zum selbstständigen Speichern. Eine erzeugte Notiz ist nicht automatisch lokal gespeichert.

## Zurückkommen und weitermachen

> Machen wir weiter. Heute habe ich 15 Minuten.

Behalte denselben Lernordner oder gib im neuen Chat deine zuletzt gespeicherte Notiz an. Koji nutzt relevante frühere Belege, um eine kurze Wiederholung und die nächste Buchaufgabe vorzuschlagen. Zum Beispiel kann eine Unterscheidung, die du mit einem Hinweis verstanden hast, vor dem Weiterlernen kurz ohne Hilfe geprüft werden.

Sag nach einer Pause einfach Bescheid:

> Ich habe eine Woche nicht gelernt. Heute habe ich 10 Minuten.

Koji beginnt beim bestätigten Fortschritt und verkleinert die Aufgabe passend zur Zeit. Aus verpassten Tagen werden keine verpflichtenden zusätzlichen Nachholstunden. Du kannst auch einen Wochenrückblick anfordern, einen Eintrag korrigieren, deine aktuelle Notiz exportieren oder sagen: „Speichere diese Sitzung nicht.“

## Deine Notizen wachsen mit deinem Lernen

Der Leitfaden ist die Starterkultur; dein Lernen liefert das Material. Wiederkehrende nützliche Erklärungen können zu verknüpften Wissensseiten werden, getrennt von Belegen dafür, was du beantworten kannst. Du musst weder Ordner organisieren noch selbst ein zweites Notizbuch führen.

Deine Lerndateien liegen unter `local/`, das standardmäßig von Git ausgeschlossen ist. Behalte diesen Ordner beim Aktualisieren von Koji; ersetze die gemeinsamen Leitfadendateien, nicht deine Lernaufzeichnungen. Lokale Speicherung bedeutet keine Offline-Verarbeitung durch die KI. Koji arbeitet während deiner Gespräche, ohne Erinnerungen im Hintergrund oder automatische Synchronisierung zwischen Kopien.

Erklärungen und Notizen richten sich nach deinen Spracheinstellungen, mit japanischen Beispielen und Kanji-Lesungen. Der Leitfaden ist auf Englisch geschrieben. Die README-Übersetzungen wurden von KI erstellt und nicht unabhängig von Muttersprachlern geprüft; die englische Fassung ist maßgeblich.

## README-Sprachen

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
