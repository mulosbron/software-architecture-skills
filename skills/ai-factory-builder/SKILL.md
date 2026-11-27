---
name: ai-factory-builder
description: Notion'un "İşin Yeni Biçimi" metodolojisini uygular. Tekrarlanan bir iş akışını özel, ortak ve denetlenen bir AI fabrikasına dönüştürür. "Fabrika kuralım", "bu iş akışını otomatikleştirelim", "bu süreç ajanla yapılabilir mi", "eval seti oluşturalım" isteklerinde veya ekibin iş listesinden otomasyon adayı çıkarılması istendiğinde tetiklenir.
---

# AI Fabrika Kurucu

Bu skill, tekrarlanan bir işin kökünü kurcalamak yerine onu özel, ortak ve denetlenen bir AI fabrikasına dönüştürür. Kaynak, Notion'un "İşin Yeni Biçimi" rehberidir. Fabrika tanımı üç ölçüte dayanır: özeldir, ortaktır ve denetlenir. Bu üçlünün hiçbirini taşımayan düzenleme fabrika değildir, kişiye özel ajan iş akışıdır.

## Ne Zaman Kullanılır

Kullanıcı şunlardan birini isterse devreye gir:

- "Bu iş akışını otomatikleştirelim" ya da "bu süreç ajanla yapılabilir mi"
- "Ekip işlerimizden fabrika adayı çıkaralım"
- "Fabrika kurma planı yaz", "eval seti hazırla", "gölge çalıştırma planı çıkar"
- Belirli bir görev türünün ajanla tekrar tekrar yapılmasını isteme

## Önce Üç Ölçütü Doğrula

Bir düzenlemenin fabrika sayılması için üç koşul bir arada olmalı:

- **Özel (specific).** Belirli türdeki görevleri üstlenmek üzere tasarlanmıştır. Gelen kutusu ayıklamadan strateji beyin fırtınasına kadar her işi isteyen bir ajan özel değildir ve fabrika sayılmaz.
- **Ortak (shared).** Ekibin birden çok insanı kullanabilir. Kurucunun yararlandığı bellek veya özel yönergeler ise ortak değildir.
- **Denetlenen (scrutinized).** Ekipten belirli kişiler ajanın çıktısını izler, hataları ayıklar ve sistemi zamanla iyileştirir. Kimsenin izlemediği bir ajan denetlenmemiştir ve fabrika sayılmaz.

Bu üçünü her teklifte açıkça doğrula ve raporda durumunu belirt.

## Adım 0: Bağlam Sistemi Önkoşulu

Fabrika, besleneceği bir bağlam sistemi olmadan iyi çalışmaz. Kurulum öncesi şu çekirdek veritabanlarının varlığını kontrol et (detaylar `docs/baglam-sistemi-ontolojisi.md` içinde):

- Projeler, Görevler, Dokümanlar, Kişiler, Ekipler, Müşteriler

Nesneler arası ilişkiler kritiktir. Görevler bir projeye bağlıdır, projelerin bir DRI'si (Doğrudan Sorumlu Kişi) Kişiler veritabanından gelir, toplantılar projelere ve katılımcılara bağlanır. Bu yapı yoksa önce en yalın hâliyle kur, sonra fabrikaya geç. Güncel olmayan ya da yanlış yerde duran bağlam, fabrikayı da zehirler (bağlam çürümesi).

## Dört Adım

### 1. Fark Et

Fabrika adayını bul. Adayların taşıdığı yedi nitelik var: tekrarlanır, doğrulanabilir, zamanla kararlı, ortalama kalite yeterli, tamamıyla dijital, bilinen bir bilgi evreni, düşük hata maliyeti. Adayı `scripts/factory_blueprint.py check` ile puanla (kullanım aşağıda). Niteliklerin ayrıntısı `docs/aday-nitelikleri.md` içindedir.

Kural: altı ve yedi puan güçlü aday, dört ve beş puan koşullu aday (eksik nitelikleri kullanıcıyla konuş), üç ve altı puan zayıf aday. Zayıf adaylarda otomasyona girişme, elle yapmaya devam etmenin gerekçesini yaz.

Amaç insanları süreçten atmak değildir. Onları montaj hattının üstündeki sorumluluk ve yetki mevkiine taşımaktır.

### 2. Planla

Yalın planla, karmaşıklığı sonra ekle. İnsanların ve LLM'lerin en sık yaptığı hata, hayal edilen hatalar için önleyici düzeltmelerle dolu karmaşık bir fabrika kurmaktır. Fabrikanın nasıl çökeceğini kimse doğru tahmin edemez. Gerçek hataları gör, sonra çöz.

Planın en temel kararları şunlardır:

- Fabrika ne yapacak, ne yapmayacak?
- Nerede yaşayacak? (veritabanı, platform, kod)
- Girdiler, aşamalar ve son çıktılar neler?
- Ajan hangi araçlara ve sistemlere erişecek?

Kurulum biçimi için melez yaklaşımı öner: görevleri, durumları, çıktıları, çalıştırma geçmişini ve istemleri esnek bir bağlam sisteminde tut, ajanın kendisini uygun bir yerde çalıştır (Notion custom agents, Claude Managed Agents, OpenAI Agents API ya da kendi kurulumun).

`scripts/factory_blueprint.py blueprint` komutu bu kararları plan iskeletine dönüştürür.

### 3. Çalıştır

İlk andan önemli ve sonuç doğuran işler verme. İki araç kullan:

- **Gölge çalıştırma.** Fabrikadan gerçek dünyada iz bırakan hiçbir şey isteme. E-posta göndermek yerine taslak yazdır, CRM'de değişiklik yapmak yerine ne yazardı onu raporla.
- **Hacim kontrolü.** Başlangıçta küçük bir örnek çalıştır. İstersen iki düzine test örneğinden oluşan bir eval setiyle başla. Güven büyüdükçe hacmi ve eylem yetkisini kademeli artır.

### 4. İyileştir

Gözlemlediğin her hatada istemi güncelle. İstem sürümlerini sakla (basit durumlarda bir Prompt Versions veritabanı yeter, resmi sürüm kontrolü çoğu fabrika için abartıdır). Yeni istemi herkesi geçirmeden önce test et.

Kritik uyarı: yalnızca son başarısızlığı test etmek yetmez. İstem değişiklikleri başka yerlerde beklenmedik sonuç doğurur. Bu yüzden görevleri ve yargı ölçütlerini yazılı hâle getir (eval). Eval setinde her görev için doğru olmasını istediğin şeyler açıkça listelenir. Bazen AI, hatta sabit kod, yargıç olabilir. Kritik çıktılarda insan bakar.

## En Yalın Fabrika Tarifi

En yalın hâli beş dakikada kurulur:

1. "Sunumlar" gibi görev türünün adıyla bir veritabanı aç.
2. "durum" sütunu ekle: yapılacak, yapılıyor, bitti.
3. "yapılacak" durumunda yeni görev oluştuğunda çalışacak bir ajan kur (platformun kendi ajan özelliği ya da webhook ile harici ajan).
4. Ajan kartı "yapılıyor"a çeksin, işi üretsin, karta çıktının bağlantısını yazıp "bitti"ye taşıyın.
5. Çalıştığını gördüğünde erişimi ekibe aç ve ekip ajanlarına "sunum istekleri bu veritabanına satır olarak düşsün" yönergesini ver.
6. Her hatada istemi güncelle.

## Script Kullanımı

```bash
# Aday puanlama: nitelikleri açıkça ver
python3 scripts/factory_blueprint.py check --name "Haftalık proje raporu" \
  --recurring evet --verifiable evet --stable evet --standard evet \
  --digital evet --known-universe evet --low-cost-mistakes evet

# Aday puanlama: serbest metinden otomatik tahmin
python3 scripts/factory_blueprint.py check --name "Sunum paketi" \
  --describe "Her hafta ekiplerin durumunu topluyoruz ve aynı format sunum üretiyoruz. Hataları kolay fark ediyoruz."

# Plan iskeleti üret
python3 scripts/factory_blueprint.py blueprint --name "Sunum paketi" \
  --trigger "veritabanında yeni kart, durum = yapılacak" \
  --stages "araştırma,yazma,tasarım" \
  --tools "bağlam sistemi okuma-yazma, sunum şablonu" \
  --out /tmp/sunum-fabrikasi-plani.md
```

Script puanı ve gerekçeleri yazdırır, plan iskeletini verilen yola kaydeder. Puan karar yerine karar desteğidir, nihai karar kullanıcıyla konuşularak verilir.

## Çıktı Formatı

Fabrika kurma sürecinin her çıktısı üç bölüm taşır:

- **Ölçüt raporu.** Özel, ortak, denetlenen üçlüsünün durumu ve yedi nitelik puanı.
- **Plan belgesi.** Görev tanımı, tetikleyiciler, girdi/aşama/çıktı, araç erişimi, gölge çalıştırma ve hacim planı.
- **İyileştirme seti.** Eval görev listesi, her görev için yargı ölçütleri ve istem sürümleme düzeni.

## Sınırlar ve Etik

- Gizli veri, üretim ortamı değişikliği ve parasal işlemler içeren adaylarda gölge çalıştırma olmadan canlıya geçilmez. Bu sınır kullanıcı isterse bile açık onay istenerek aşılar.
- Yedi nitelik ve üç ölçüt dışında uydurma gerekçe üretilmez. Puan düşükse düşük denir.
- Fabrika taslağındaki isimler, veritabanları ve adımlar kullanıcının gerçek araçlarına uyarlanır. Uyarlanamayan yerde varsayım açıkça işaretlenir.
- Amaç işten insanı çıkarmak değildir. Rapor bu ilkeyi taşımalıdır.
