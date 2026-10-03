# Koji — JLPT Study Agent

Kendi ders kitabınızla, kendi dilinizde JLPT N5–N1 sınavlarına çalışın. Zor bir soruda yardım alın, bugüne uygun görevler seçin ve kaldığınız yerden devam edin.

## Bir soruyla başlayın

**Mevcut bir yapay zekâ sohbetinde:** [Koji rehberini](../agent/COACH.md) yükleyin veya yapıştırın, ardından sorunuzu gönderin. Gerektiğinde ilgili cümleyi, seçenekleri ve kendi yanıtınızı ekleyin. Kısa bir alıntı veya sohbetinizin işleyebileceği okunaklı bir fotoğraf kullanın.

> Bu Koji rehberini uygula. Türkçe açıkla. B'yi seçtim ama cevap anahtarı C diyor. İşte metin ve gerekçem. C neden daha uygun?

**Dosya erişimi olan Codex veya Claude Code içinde:** [bu depoyu indirin](https://github.com/youngtak-k/koji-jlpt-study-agent/archive/refs/heads/main.zip), arşivi açın ve klasörü açın. Şunu yazın:

> AGENTS.md dosyasını oku ve Koji ile çalışmama yardım et. Türkçe açıkla ve notlarımı Türkçe tut. İşte ders kitabımdaki sorum.

Her iki isteği de kendi dilinizde yazabilirsiniz. Koji sunucusu, ayrı bir uygulama, Python kurulumu veya projeye özel API anahtarı gerekmez. Rehberi okuyabilen bir yapay zekâ asistanına erişiminiz olmalıdır; asistanın sınırları ve ücretleri geçerli olmaya devam eder.

## Ya da bugünkü çalışmanızı seçin

Koji'ye kitabın hangi bölümünün açık olduğunu ve ne kadar zamanınız olduğunu söyleyin. Hedef JLPT seviyeniz henüz bilinmiyorsa onu da ekleyin.

> N3'e çalışıyorum. Bu dil bilgisi bölümünün başındayım ve 25 dakikam var. Bugünkü çalışmamı seçmeme yardım et.

Koji bir başlangıç noktası, bir bitiş noktası ve tekrar, sorular ile kısa bir kapanışı içeren zaman planı önerir. Yalnızca kitap adı, sayfalarını veya içeriğini belirlemek için yeterli değildir. Tüm sınav için plan yapmadan önce tek bir bölümle başlayabilirsiniz.

## Tek mesajla bitirin

> 1–4. soruları 18 dakikada bitirdim. 3. soru için ipucu gerekti. Sırada 5. soru var.

Koji gerçekten yaptıklarınızı, belirsiz kalan noktaları ve nereden devam edeceğinizi özetler. Soru sormak otomatik olarak hata sayılmaz; ipucuyla verilen yanıt, bağımsız yanıttan ayrı tutulur.

Dosya erişimi çalışıyorsa Koji güncel kaydınızı `local/CURRENT.md` konumuna kaydeder ve doğrular; oturum notları bu kaydı destekler. Sıradan bir sohbette ise kendiniz kaydetmeniz için kısa, güncellenmiş bir çalışma notu verir. Bir notun üretilmesi, otomatik olarak yerel dosyaya kaydedildiği anlamına gelmez.

## Geri gelin ve devam edin

> Devam edelim. Bugün 15 dakikam var.

Aynı çalışma klasörünü koruyun veya yeni sohbete en son kaydettiğiniz notu verin. Koji ilgili önceki sonuçları kullanarak kısa bir tekrar ve kitaptaki sonraki görevi önerir. Örneğin, ipucuyla anladığınız bir ayrım, ilerlemeden önce kısa ve bağımsız bir soruyla kontrol edilebilir.

Ara verdiyseniz bunu söyleyin:

> Bir hafta çalışmadım. Bugün 10 dakikam var.

Koji doğrulanmış ilerlemenizden başlar ve görevi süreye sığacak şekilde küçültür. Kaçırılan günler, zorunlu telafi için ek saatlere dönüşmez. Ayrıca haftalık değerlendirme isteyebilir, bir kaydı düzeltebilir, güncel notunuzu dışa aktarabilir veya “bu oturumu kaydetme” diyebilirsiniz.

## Notlarınız çalışmanızla birlikte büyür

Rehber maya görevi görür; malzemeyi sizin çalışmanız sağlar. Tekrar ihtiyaç duyulan yararlı açıklamalar, hangi soruları yanıtlayabildiğinize ilişkin kanıtlardan ayrı tutulan bağlantılı bilgi sayfalarına dönüşebilir. Klasörleri kendiniz düzenlemeniz veya ikinci bir defter tutmanız gerekmez.

Çalışma dosyalarınız, varsayılan olarak Git dışında tutulan `local/` altında kalır. Koji'yi güncellerken bu klasörü koruyun; öğrenme kayıtlarınızı değil, ortak rehber dosyalarını değiştirin. Yerel depolama, yapay zekâ işlemlerinin çevrimdışı yapıldığı anlamına gelmez. Koji sohbetleriniz sırasında çalışır; arka planda hatırlatmalar yapmaz veya kopyalar arasında otomatik eşitleme sağlamaz.

Açıklamalar ve notlar, Japonca örnekler ve kanji okumalarıyla birlikte dil tercihlerinize uyar. Rehber İngilizce yazılmıştır. README çevirileri yapay zekâ tarafından hazırlanmıştır ve bağımsız bir ana dili konuşuru incelemesinden geçmemiştir; İngilizce sürüm referanstır.

## README dilleri

[İngilizce referans sürüm](../README.md) · [Tüm README dilleri](../README.md#readme-languages)

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
