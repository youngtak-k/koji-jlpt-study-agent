# Koji — JLPT Study Agent

Przygotowuj się do JLPT N5–N1 z własnym podręcznikiem, we własnym języku. Uzyskaj pomoc przy trudnym pytaniu, wybierz zadania na miarę dzisiejszego czasu i wróć do miejsca, w którym skończyłeś naukę.

## Zacznij od pytania

**W dotychczasowym czacie z AI:** prześlij lub wklej [przewodnik Koji](../agent/COACH.md), a następnie zadaj pytanie. W razie potrzeby dołącz odpowiednie zdanie, warianty odpowiedzi i swoją odpowiedź. Użyj krótkiego fragmentu lub czytelnego zdjęcia, które Twój czat potrafi przetworzyć.

> Stosuj się do tego przewodnika Koji. Wyjaśniaj po polsku. Moja odpowiedź to B, ale klucz wskazuje C. Oto fragment i moje rozumowanie. Dlaczego C pasuje lepiej?

**W Codex lub Claude Code z dostępem do plików:** [pobierz to repozytorium](https://github.com/youngtak-k/koji-jlpt-study-agent/archive/refs/heads/main.zip), rozpakuj je i otwórz folder. Napisz:

> Przeczytaj AGENTS.md i pomóż mi uczyć się z Koji. Wyjaśniaj po polsku i prowadź moje notatki po polsku. Oto pytanie z mojego podręcznika.

Oba polecenia możesz napisać we własnym języku. Nie potrzebujesz serwera Koji, osobnej aplikacji, instalacji Pythona ani klucza API dla projektu. Potrzebujesz dostępu do asystenta AI, który potrafi przeczytać przewodnik; nadal obowiązują jego limity i opłaty.

## Albo wybierz zadania na dziś

Powiedz Koji, którą część podręcznika masz otwartą i ile masz czasu. Dodaj docelowy poziom JLPT, jeśli nie jest jeszcze znany.

> Przygotowuję się do N3. Jestem na początku tej części poświęconej gramatyce i mam 25 minut. Pomóż mi wybrać zadania na dziś.

Koji proponuje punkt rozpoczęcia, punkt zakończenia oraz podział czasu uwzględniający powtórkę, pytania i krótkie podsumowanie. Sam tytuł podręcznika nie wystarcza, by ustalić jego strony lub treść. Możesz zacząć od jednej części, zanim ułożysz plan przygotowań do całego egzaminu.

## Zakończ jedną wiadomością

> Zadania 1–4 są skończone; zajęły 18 minut. Przy zadaniu 3 potrzebna była podpowiedź. Następne jest zadanie 5.

Koji podsumowuje faktycznie wykonaną pracę, to, co pozostaje niepewne, i miejsce wznowienia nauki. Zadanie pytania nie liczy się automatycznie jako błąd; odpowiedź z podpowiedzią pozostaje odrębna od samodzielnej.

Gdy dostęp do plików działa, Koji zapisuje i sprawdza bieżący zapis w `local/CURRENT.md`, wraz z pomocniczymi notatkami z sesji. W zwykłym czacie udostępnia zwięzłą, zaktualizowaną notatkę z nauki do samodzielnego zapisania. Wygenerowanie notatki nie oznacza automatycznego zapisu lokalnego.

## Wróć i kontynuuj

> Kontynuujmy. Mam dziś 15 minut.

Zachowaj ten sam folder do nauki albo przekaż najnowszą zapisaną notatkę w nowym czacie. Koji wykorzystuje odpowiednie wcześniejsze wyniki, by zaproponować krótką powtórkę i następne zadanie z podręcznika. Na przykład różnicę zrozumianą wcześniej z podpowiedzią można krótko sprawdzić samodzielnie przed przejściem dalej.

Po przerwie powiedz o niej:

> Przez tydzień nie było nauki. Mam dziś 10 minut.

Koji zaczyna od potwierdzonych postępów i zmniejsza zadanie do dostępnego czasu. Opuszczone dni nie zamieniają się w dodatkowe godziny obowiązkowego nadrabiania. Możesz też poprosić o podsumowanie tygodnia, poprawić zapis, wyeksportować bieżącą notatkę lub powiedzieć „nie zapisuj tej sesji”.

## Twoje notatki rosną wraz z nauką

Przewodnik działa jak zakwas; Twoja nauka dostarcza mu materiału. Przydatne wyjaśnienia, do których wracasz, mogą stać się powiązanymi stronami wiedzy, oddzielonymi od dowodów na to, na co potrafisz odpowiedzieć. Nie musisz samodzielnie porządkować folderów ani prowadzić drugiego zeszytu.

Pliki do nauki pozostają w `local/`, domyślnie wyłączonym z Git. Zachowaj ten folder podczas aktualizacji Koji: zastępuj wspólne pliki przewodnika, a nie swoje zapisy z nauki. Przechowywanie lokalne nie oznacza przetwarzania przez AI bez internetu. Koji działa podczas Twoich rozmów, bez przypomnień w tle i automatycznej synchronizacji między kopiami.

Wyjaśnienia i notatki uwzględniają Twoje preferencje językowe oraz zawierają japońskie przykłady i odczyty kanji. Przewodnik jest napisany po angielsku. Tłumaczenia README zostały opracowane przez AI i nie przeszły niezależnej weryfikacji przez rodzimych użytkowników języka; wersją odniesienia jest angielska.

## Języki README

[Angielska wersja odniesienia](../README.md) · [Wszystkie języki README](../README.md#readme-languages)

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
