# Örnek Fabrikalar

İlham için kurulmuş ya da başarıyla kurulmuş gördüğü fabrikalardan derlenmiş bir set. Her örnek için üç ölçütün (özel, ortak, denetlenen) nasıl karşılandığına dikkat et.

## Beş tipik fabrika tipi

1. **Müşteri deneyimi fabrikası.** Müşteriler destek ekibine e-posta yazar ya da sohbet açar. Bir ajan işi kendi başına yürütür, bazı durumlarda konuyu bir insana yükseltmeye karar verir.
2. **Sunum paketi fabrikası.** Aynı tür sunumu defalarca üretmek zorunda kalan ekipler için standartlaştırılmış sonuç üreten ortak sistem.
3. **Hata düzeltme fabrikası.** Yazılım çökmeleri üretimde yakalanır ve ajan tetiklenir. Ajan araştırır, düzeltir ve pull request açar. Adversarial inceleme ajanları güvenli görürse birleştirir.
4. **Veri fabrikası.** Ekip veri sorusu sorar ("Geçen hafta kaç sipariş geldi?"). Ajan açıklığa kavuşturucu sorular sorar, veri ambarına girer ve görsel, etkileşimli bir sunum kurar. İnsan uzmanlar örnekleri gözden geçirip ajanın davranışını ayarlar.
5. **Müşteri kabul fabrikası.** Yeni müşteri imzalandığında birden çok eylemi tetikleyen süreç. Zekâ ister ama her seferinde tam olarak aynı biçimde gerçekleşmesi istenir.

## Kurulmuş fabrika fikirleri listesi

- Müşteri destek e-postalarını yanıtlama
- E-posta bültenlerinin kalite kontrolü
- Yazılım bağımlılıklarını güncel tutma
- Küçük hataları düzeltme
- Veri sorularını yanıtlama
- Basit tanıtım videoları üretme
- Haftalık proje güncellemeleri
- Satış takibi
- Ürün geri bildirimlerini işleme ve önceliklendirme
- Çalışan işe alıştırma
- Fatura ve gider işleme

## Eval seti örneği: sunum paketi fabrikası

Eval, AI'ın üstün olmasını istediğin görevleri ve her birinde performansı yargılayacağın ölçütleri yazılı hâle getiren listedir. Yalnızca son başarısızlığı test etmek yetmez, çünkü istem değişiklikleri başka yerlerde beklenmedik sonuç doğurur.

| Görev | Yargı ölçütleri | Yargıç |
|---|---|---|
| 20 slaytlık satış sunumu | Başlık en fazla 6 kelime, şirketin tonu, zorunlu fiyat tablosu var | Kod (uzunluk) + insan (ton) |
| 3 slaytlık yürütme özeti | Bir ana mesaj, rakamlar veri ambarından ve güncel | Kod + insan |
| Şablon dışı istek (negatif test) | Fabrika talebi reddediyor ya da insan onayına düşürüyor | Kod |

Negatif testin yerini vurgula: istem değişikliğinin başlıkları kısaltırken diğer metinleri de kısaltmadığından emin olmanın yolu, görev setini her çalıştırmada tam tur döndürmektir.

## Gölge çalıştırma örneği: destek e-posta fabrikası

- Aşama 1: fabrika hiçbir e-postaya dokunmaz, her gelen e-posta için ne yazardı diye taslak hazırlar ve bir tabloya düşer.
- Aşama 2: insanlar tablodaki taslakların %20'sini gözden geçirir, hata türlerini etiketler.
- Aşama 3: hata oranı eşiğin altına inince hacim %5'e çıkar, sonra %25, sonra %100.
- İstemediğin senaryo: birinci günde bir milyon e-postanın hepsine taslak yazdırmak.
