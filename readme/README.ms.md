# Koji — JLPT Study Agent

Belajar untuk JLPT N5–N1 dengan buku teks anda sendiri, dalam bahasa anda. Dapatkan bantuan untuk soalan sukar, pilih tugasan yang sesuai dengan masa hari ini, dan sambung dari tempat anda berhenti.

## Mulakan dengan soalan

**Dalam sembang AI yang sudah anda gunakan:** muat naik atau tampal [panduan Koji](../agent/COACH.md), kemudian hantar soalan. Sertakan ayat berkaitan, pilihan jawapan dan jawapan anda apabila perlu. Gunakan petikan pendek atau foto yang jelas dan boleh diproses oleh sembang anda.

> Ikuti panduan Koji ini. Terangkan dalam bahasa Melayu. Saya memilih B, tetapi skema jawapan menyatakan C. Ini petikan dan alasan saya. Mengapa C lebih sesuai?

**Dalam Codex atau Claude Code dengan akses fail:** [muat turun repositori ini](https://github.com/youngtak-k/koji-jlpt-study-agent/archive/refs/heads/main.zip), nyahzip dan buka folder. Minta:

> Baca AGENTS.md dan bantu saya belajar dengan Koji. Terangkan dan tulis nota saya dalam bahasa Melayu. Ini soalan saya daripada buku teks.

Anda boleh menulis kedua-dua permintaan dalam bahasa sendiri. Pelayan Koji, aplikasi berasingan, pemasangan Python atau kunci API projek tidak diperlukan. Anda memerlukan akses kepada pembantu AI yang boleh membaca panduan; had dan kos perkhidmatan itu masih terpakai.

## Atau pilih tugasan hari ini

Beritahu Koji bahagian buku yang sedang dibuka dan berapa banyak masa yang ada. Tambahkan tahap sasaran JLPT jika belum diketahui.

> Saya sedang bersedia untuk N3. Saya berada di awal bahagian tatabahasa ini dan ada 25 minit. Bantu saya memilih tugasan hari ini.

Koji mencadangkan titik mula, titik berhenti dan pembahagian masa termasuk ulang kaji, soalan dan penutup ringkas. Tajuk buku sahaja tidak cukup untuk menentukan halaman atau kandungannya. Anda boleh bermula dengan satu bahagian sebelum membuat rancangan untuk seluruh peperiksaan.

## Akhiri dengan satu mesej

> Saya menyiapkan soalan 1–4 dalam 18 minit. Saya memerlukan petunjuk untuk soalan 3. Seterusnya soalan 5.

Koji merumuskan apa yang benar-benar anda buat, apa yang masih belum pasti dan tempat untuk menyambung. Bertanya tidak secara automatik dikira sebagai kesilapan; jawapan dengan petunjuk tetap dibezakan daripada jawapan sendiri.

Apabila akses fail berfungsi, Koji menyimpan dan menyemak rekod semasa di `local/CURRENT.md`, bersama nota sesi sokongan. Dalam sembang biasa, ia memberikan nota belajar ringkas yang dikemas kini untuk anda simpan sendiri. Nota yang dijana tidak bermakna ia disimpan secara automatik pada peranti anda.

## Kembali dan sambung

> Mari sambung. Hari ini saya ada 15 minit.

Kekalkan folder belajar yang sama atau berikan nota terakhir yang disimpan dalam sembang baharu. Koji menggunakan bukti terdahulu yang berkaitan untuk mencadangkan ulang kaji pendek dan tugasan buku seterusnya. Contohnya, perbezaan yang difahami dengan petunjuk boleh diuji secara ringkas tanpa bantuan sebelum anda meneruskan.

Selepas berehat, nyatakannya:

> Saya tidak belajar selama seminggu. Hari ini saya ada 10 minit.

Koji bermula daripada kemajuan yang disahkan dan mengecilkan tugasan mengikut masa. Hari yang terlepas tidak menjadi jam tambahan wajib untuk mengejar ketinggalan. Anda juga boleh meminta semakan mingguan, membetulkan rekod, mengeksport nota semasa atau berkata “jangan simpan sesi ini”.

## Nota berkembang bersama pembelajaran

Panduan ini seperti kultur pemula; pembelajaran anda membekalkan bahannya. Penjelasan berulang yang berguna boleh menjadi halaman pengetahuan berpaut, berasingan daripada bukti tentang apa yang anda boleh jawab. Anda tidak perlu menyusun folder atau menyelenggara buku nota kedua sendiri.

Fail pembelajaran anda kekal di bawah `local/`, yang dikecualikan daripada Git secara lalai. Kekalkan folder ini semasa mengemas kini Koji; gantikan fail panduan bersama, bukan rekod pembelajaran anda. Storan setempat tidak bermakna pemprosesan AI di luar talian. Koji bekerja semasa perbualan, tanpa peringatan latar belakang atau penyegerakan automatik antara salinan.

Penjelasan dan nota mengikut pilihan bahasa anda, dengan contoh bahasa Jepun dan bacaan kanji. Panduan ditulis dalam bahasa Inggeris. Terjemahan README ditulis oleh AI dan belum disemak secara bebas oleh penutur asli; edisi Inggeris ialah rujukan.

## Bahasa README

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
