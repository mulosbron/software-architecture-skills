# Bağlam Sistemi Ontolojisi

Fabrika, besleneceği bir bağlam sistemi olmadan iyi çalışmaz. Bu dosya, fabrika kurulumundan önce ya da beraberinde kurulacak bağlam sisteminin en yalın sağlam yapısını tanımlar.

## Bağlam sisteminin altı işi

1. Şirketin tüm temel bilgi ve birikimini saklar.
2. Her şeyin düzenli olmasını ve mantıklı bir yerine gitmesini sağlar.
3. Her şeyi ayrıntı izinler ve sürüm kontrolleriyle yönetir.
4. Bilgiyi istediğin her biçimde gösterir.
5. Ekibe iyi bir iş birliği deneyimi sunar: yorum, bildirim, mobil, masaüstü.
6. Herhangi bir ajanla kusursuz çalışır.

## Çekirdek veritabanları

Karmaşık bir ontolojiyle başlama. Küçük bir çekirdek setle başla ve ilişkileri ona kur:

| Veritabanı | Tipik nitelikler | Bağlandığı yerler |
|---|---|---|
| Projeler | Ad, durum, DRI (Doğrudan Sorumlu Kişi), tarih aralığı | Görevler, Dokümanlar, Toplantılar, Müşteriler |
| Görevler | Ad, durum (yapılacak/yapılıyor/bitti), sorumlu, proje | Projeler, Kişiler |
| Dokümanlar | Ad, tür, sahibin, sürüm | Projeler, Kişiler |
| Kişiler | Rol, yönetici (org şeması çıkarır), ekip | Ekipler, Projeler |
| Ekipler | Ad, üyeler | Kişiler, Projeler |
| Müşteriler | Ad, durum, iletişim kişisi | Projeler, Toplantılar |

Org şeması gibi çıktılar bu ilişkilerden kendiliğinden çıkar. Kod bilmeden, sistemlerle düşünerek kurulur.

## Fraktal yapı

Çekirdek dışındaki tek seferlik veritabanları da biraz yapı taşır. Sürümlü bir rehber belgesi bile sürüm numarası ve zaman damgası taşıyan bir taslak izleyiciden geçebilir. İki sürümün farkını merak eden kişi ajanına sorar ve ajan yapıyı takip ederek cevabı bulur. Düzen kurmayı kolaylaştırmak, bağlam sisteminin varsayılan davranışı olmalı.

## Senkronlar

Bilgiyi merkeze taşımak için iki yol vardır:

- **Yönetilen senkronlar.** Bağlam sistemi kaynağı resmen yönetir (örnek: Salesforce, Slack, takvim).
- **İşçi senkronlar.** Yönetilen senkronu olmayan kaynaklar için, ajanla ya da kodla kurulan özel çekme düzeni.

Dış sistemleri kullanmaya devam edebilirsin ama ajanlara düzinelerce kaynağa doğrudan erişim vermek karmaşıklık ekler, hata noktalarını çoğaltır ve yönetilebilirliği katlanarak zorlaştırır. Senkronla. Hedef, tüm iç işleyiş verisinin tek bir yönetilmiş erişim noktasında toplanmasıdır. İstersen buna bağlam ambarı de.

## İzinler

- Kişi grupları tanımla ve erişimi gruba ver, tek tek kişilere değil. Gruplar zamanla değişir (katılım, terfi) ve grup tabanlı izin otomatik uyar.
- Hassas tek bir bilgi parçası için tüm veritabanını kopyalama. Sütun tabanlı izin yeterliyse sütun kullan.
- Satır tabanlı izinle bir kişi yalnızca kendi kaydını görebilir (örnek: kendi yazdığı performans değerlendirmeleri).

## Doğrulama

Bağlam sistemi, belirli türde kötü bilgiyi içeri sokmayı engellemelidir. Zorunlu alanlar, biçim kontrolleri, ürün notlarının ana soruları cevaplayıp cevaplamadığını test eden kontroller, dağınık sayfaların doğru yere fişlenmesi ve yeni kararların tüm sayfalara yansıması bunun ileri hâlleridir.

## Bağlam çürümesi

Bir numaralı düşman kötü bağlamdır: bayat, eksik, yanlış örgütlenmiş, yanlış yerde ve güncelliğini yitirmiş bilgi. Ajanlar sayesinde bu temizlik artık sürekli hâle getirilebilir. Fabrika kurulurken bağlam çürümesi kontrolünü de plana ekle: hangi bilgiler ne sıklıkla taranır, bayatlık nasıl işaretlenir, kim düzeltir.
