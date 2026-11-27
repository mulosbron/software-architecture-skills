# Fabrika Adayı Nitelikleri

Bir işin fabrika olmaya uygunluğu yedi nitelik üzerinden değerlendirilir. `scripts/factory_blueprint.py check` bu nitelikleri puanlar. Amaç insanları süreçten atmak değildir. Onları rutin işin montaj hattı üstündeki sorumluluk ve yetki mevkiine taşımaktır. Kullanıcı bu bakışı raporda görmeli.

## Yedi nitelik

1. **Tekrarlanır.** İş aynı biçimde tekrar tekrar gelir. Haftalık rapor, günlük destek e-postası, sürüm bağımlılık güncellemesi bu gruptadır.
2. **Doğrulanabilir.** Çıktının iyi olup olmadığı bir ölçütle söylenebilir. Başlık uzunluğu, ton, zorunlu alanlar gibi. Doğrulanmayan işte eval kurulamaz.
3. **Zamanla kararlı.** Süreç ve gereksinimler görece sabittir. Her seferinde bambaşka sorulan bir iş fabrika için zayıf adaydır.
4. **Ortalama kalite yeterli.** İstisnai dahi yaratıcılık değil, standart ve güvenilir bir düzey hedeftir. Pekala, burada insan özgünlüğü merkezdeyse otomasyon hedefi yanlıştır.
5. **Tamamıyla dijital bilgi işi.** Robotik ve fiziksel dünya bu metodolojinin kapsamı dışındadır.
6. **Bilinen bir bilgi evreni.** Ajanın hangi kaynaklara bakacağı bellidir. Bilgi evreni her seferinde değişiyorsa ajan kaybolur.
7. **Düşük hata maliyeti.** Hatalar pahalıya gelmez ya da kolay yakalanır. Pahalı hataların yolu gölge çalıştırma ve kademeli yetkilendirmedir.

## Puan yorumu

- **6-7 puan:** güçlü aday. Plan aşamasına geç.
- **4-5 puan:** koşullu aday. Eksik niteliklerin hafifletme yolu var mı bak. Örneğin doğrulanabilirlik eksikse önce bir doğrulama ölçütü seti yaz.
- **0-3 puan:** zayıf aday. Otomasyona girişme. Elle yürütmenin gerekçesini rapora yaz.

## Fabrika ile olmayan şeyin farkı

Bir ajan düzenlemesi fabrika sayılmak için üç ölçütü birden taşımalıdır: **özel** (belirli görev türleri, hepsi değil), **ortak** (birden çok insan kullanır), **denetlenen** (belirli kişiler performansı izler ve iyileştirir).

Buna göre:

- Her işi isteyen bir kişisel ajan fabrika değildir, çünkü özel değildir.
- Yalnızca senin yararlandığın bellekli ajan fabrika değildir, çünkü ortak değildir.
- Kimse izlemediği bir ortak ajan fabrika değildir, çünkü denetlenmemiştir.

Beceri dosyaları (skill) bir tür proto-fabrikadır: yönergeleri paylaşır ama bağlamı, bilgisayarı ve denetimi paylaşmaz. Zamanla iş fabrika benzeri ortamlara taşınır.

## İnsan katılımı

Fabrika, insan gözetimi olmayan "karanlık fabrika" demek değildir. Fabrika iş akışının birçok parçası insan yaratıcılığı ve yargısı ister. Nerede ve nasıl katılacağına kullanıcı karar verir ve skill bu kararı raporda açıkça sorar.
