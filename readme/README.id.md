# Koji — JLPT Study Agent

Belajar untuk JLPT N5–N1 dengan buku Anda sendiri, dalam bahasa Anda sendiri. Dapatkan bantuan untuk soal yang sulit, pilih tugas yang sesuai dengan waktu hari ini, dan lanjutkan dari titik terakhir.

## Mulai dengan sebuah pertanyaan

**Di obrolan AI yang sudah Anda gunakan:** unggah atau tempelkan [panduan Koji](../agent/COACH.md), lalu kirim pertanyaan Anda. Sertakan kalimat terkait, pilihan jawaban, dan jawaban Anda bila diperlukan. Gunakan kutipan singkat atau foto yang jelas dan dapat diproses oleh obrolan Anda.

> Ikuti panduan Koji ini. Jelaskan dalam bahasa Indonesia. Saya memilih B, tetapi kunci jawaban menyatakan C. Berikut teks dan alasan saya. Mengapa C lebih tepat?

**Di Codex atau Claude Code dengan akses berkas:** [unduh repositori ini](https://github.com/youngtak-k/koji-jlpt-study-agent/archive/refs/heads/main.zip), ekstrak, lalu buka foldernya. Tulis:

> Baca AGENTS.md dan bantu saya belajar dengan Koji. Jelaskan dalam bahasa Indonesia dan tulis catatan saya dalam bahasa Indonesia. Berikut pertanyaan saya dari buku.

Anda dapat menulis kedua permintaan tersebut dalam bahasa Anda sendiri. Tidak diperlukan server Koji, aplikasi terpisah, instalasi Python, atau kunci API proyek. Anda memerlukan akses ke asisten AI yang dapat membaca panduan; batas penggunaan dan biayanya tetap berlaku.

## Atau pilih tugas hari ini

Beri tahu Koji bagian buku yang sedang terbuka dan waktu yang Anda miliki. Tambahkan target tingkat JLPT jika belum diketahui.

> Saya sedang belajar untuk N3. Saya berada di awal bagian tata bahasa ini dan punya waktu 25 menit. Bantu saya memilih tugas hari ini.

Koji mengusulkan titik awal, titik berhenti, dan pembagian waktu yang mencakup pengulangan, pertanyaan, serta penutup singkat. Judul buku saja tidak cukup untuk menyimpulkan halaman atau isinya. Anda dapat mulai dari satu bagian sebelum membuat rencana untuk seluruh ujian.

## Akhiri dengan satu pesan

> Saya menyelesaikan soal 1–4 dalam 18 menit. Saya membutuhkan petunjuk untuk soal 3. Berikutnya adalah soal 5.

Koji merangkum apa yang benar-benar Anda kerjakan, hal yang masih belum pasti, dan titik untuk melanjutkan. Mengajukan pertanyaan tidak otomatis dihitung sebagai kesalahan; jawaban dengan petunjuk tetap dibedakan dari jawaban mandiri.

Jika akses berkas berfungsi, Koji menyimpan dan memeriksa catatan terkini Anda di `local/CURRENT.md`, dengan catatan sesi sebagai pendukung. Dalam obrolan biasa, Koji memberikan catatan belajar terbaru yang ringkas untuk Anda simpan sendiri. Catatan yang dihasilkan tidak otomatis tersimpan secara lokal.

## Kembali dan lanjutkan

> Lanjutkan. Saya punya waktu 15 menit hari ini.

Gunakan folder belajar yang sama, atau berikan catatan terakhir yang Anda simpan di obrolan baru. Koji menggunakan bukti belajar sebelumnya yang relevan untuk menyarankan pengulangan singkat dan tugas buku berikutnya. Misalnya, perbedaan yang Anda pahami dengan bantuan petunjuk dapat diperiksa sebentar secara mandiri sebelum melanjutkan.

Setelah jeda, sampaikan hal itu:

> Saya tidak belajar selama seminggu. Saya punya waktu 10 menit hari ini.

Koji mulai dari kemajuan yang telah dikonfirmasi dan memperkecil tugas agar sesuai dengan waktu. Hari yang terlewat tidak berubah menjadi tambahan jam wajib untuk mengejar ketertinggalan. Anda juga dapat meminta tinjauan mingguan, memperbaiki catatan, mengekspor catatan terkini, atau mengatakan “jangan simpan sesi ini”.

## Catatan Anda tumbuh bersama kegiatan belajar

Panduan ini berperan sebagai biang fermentasi; kegiatan belajar Anda menyediakan bahannya. Penjelasan bermanfaat yang berulang dapat menjadi halaman pengetahuan yang saling terhubung, terpisah dari bukti tentang apa yang mampu Anda jawab. Anda tidak perlu mengatur folder atau mengelola buku catatan kedua sendiri.

Berkas belajar Anda tetap berada di `local/`, yang secara bawaan dikecualikan dari Git. Pertahankan folder ini saat memperbarui Koji; ganti berkas panduan bersama, bukan catatan belajar Anda. Penyimpanan lokal tidak berarti pemrosesan AI berlangsung luring. Koji bekerja selama percakapan Anda, tanpa pengingat di latar belakang atau sinkronisasi otomatis antar salinan.

Penjelasan dan catatan mengikuti pilihan bahasa Anda, dengan contoh bahasa Jepang dan cara baca kanji. Panduan ditulis dalam bahasa Inggris. Terjemahan README dibuat oleh AI dan belum melalui tinjauan independen oleh penutur asli; bahasa Inggris adalah edisi acuan.

## Bahasa README

[Edisi acuan bahasa Inggris](../README.md) · [Semua bahasa README](../README.md#readme-languages)

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
