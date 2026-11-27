#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
factory_blueprint.py — AI fabrika adayı puanlayıcı ve plan iskeleti üretici.

Kaynak: Notion "İşin Yeni Biçimi" metodolojisi (ai-factory-builder skill'i).

Kullanım:
    # Nitelikleri açıkça puanlat
    factory_blueprint.py check --name "Haftalık rapor" --recurring evet --verifiable evet \
        --stable evet --standard evet --digital evet --known-universe evet --low-cost-mistakes evet

    # Serbest metinden otomatik tahminle puanlat
    factory_blueprint.py check --name "Sunum paketi" --describe "her hafta aynı format sunum..."

    # Plan iskeleti üret
    factory_blueprint.py blueprint --name "Sunum paketi" --trigger "..." \
        --stages "araştırma,yazma" --tools "..." --out plan.md

Evet anahtarları: evet/yes/y/true/1  hayır/no/n/false/0
"""

import argparse
import json
import re
import sys
from pathlib import Path

YES = {"evet", "yes", "y", "true", "1", "var"}
NO = {"hayır", "hayir", "no", "n", "false", "0", "yok"}

TRAITS = [
    ("recurring", "Tekrarlanır"),
    ("verifiable", "Doğrulanabilir"),
    ("stable", "Zamanla kararlı (süreç ve gereksinimler görece sabit)"),
    ("standard", "Ortalama/standart kalite yeterli, istisnai yaratıcılık gerekmez"),
    ("digital", "Tamamıyla dijital bilgi işi"),
    ("known-universe", "Bilinen bir bilgi evrenine erişim gerektirir"),
    ("low-cost-mistakes", "Hatalar pahalıya gelmez ya da kolay yakalanır"),
]

# Serbest metinden nitelik tahmini için anahtar kelimeler (TR + EN)
HINTS = {
    "recurring": r"her (hafta|gün|ay|çeyrek)|haftalık|günlük|aylık|çeyreklik|tekrar|düzenli|weekly|daily|monthly|recurr",
    "verifiable": r"doğrula|kontrol|kalite kontrol|hata (yakala|bul)|eval|kontrol edilebilir|verify|check|evals",
    "stable": r"sabit|aynı format|aynı biçim|standart|şablon|template|değişmeyen|same format|stable",
    "standard": r"standart|yeterli|normal|ortalama|fark etmez|good enough|standard",
    "digital": r"e-?posta|mail|rapor|doküman|sunum|veri|tablo|slayt|digital|document|report|deck",
    "known-universe": r"veritabanı|crm|ambar|arşiv|arsiv|kaynak(lar)?|dizini|database|warehouse|repository",
    "low-cost-mistakes": r"kolay (fark|yakala)|düşük risk|geri alınabilir|revizyon|taslak|gölge|easy (to )?(catch|detect)|low (risk|cost)|shadow|draft",
}


def _norm(v):
    if v is None:
        return None
    v = v.strip().lower()
    if v in YES:
        return True
    if v in NO:
        return False
    return None


def infer_from_text(text):
    flags = {}
    for key, rx in HINTS.items():
        flags[key] = bool(re.search(rx, text, re.IGNORECASE))
    return flags


def score(name, flags, inferred_keys):
    score_val = sum(1 for k, _ in TRAITS if flags.get(k))
    missing = [label for key, label in TRAITS if not flags.get(key)]
    if score_val >= 6:
        verdict = "GÜÇLÜ ADAY — fabrika kurma planına geç."
    elif score_val >= 4:
        verdict = "KOŞULLU ADAY — eksik nitelikleri kullanıcıyla konuş, hafifletme yolu varsa planla."
    else:
        verdict = "ZAYIF ADAY — otomasyona girişme; elle yürütmeyi sürdürmenin gerekçesini yaz."
    lines = []
    lines.append("=" * 60)
    lines.append(f"Fabrika adayı puanı: {name}")
    lines.append("=" * 60)
    lines.append(f"Puan: {score_val}/7")
    lines.append(f"Karar: {verdict}")
    lines.append("")
    lines.append("Nitelik durumu:")
    for key, label in TRAITS:
        mark = "evet" if flags.get(key) else "hayır"
        src = "(metinden tahmin edildi)" if key in inferred_keys else ""
        lines.append(f"  [{mark:>5}] {label} {src}")
    if missing:
        lines.append("")
        lines.append("Eksik nitelikler:")
        for label in missing:
            lines.append(f"  - {label}")
    lines.append("")
    lines.append("Hatırlatma: fabrika olmanın üç ölçütü ayrıca doğrulanmalı: özel, ortak, denetlenen.")
    lines.append("=" * 60)
    return "\n".join(lines)


def cmd_check(args):
    flags = {}
    inferred_keys = set()
    for key, _ in TRAITS:
        flags[key] = _norm(getattr(args, key.replace("-", "_"), None))
    if args.describe:
        inferred = infer_from_text(args.describe)
        for key, value in inferred.items():
            if flags[key] is None:
                flags[key] = value
                inferred_keys.add(key)
    for key, _ in TRAITS:
        if flags[key] is None:
            flags[key] = False
            inferred_keys.add(key)
    print(score(args.name, flags, inferred_keys))
    return 0


BLUEPRINT = """# Fabrika Planı: {name}

## 1. Ölçüt raporu

- Özel: [bu fabrika hangi görev türünü yapar, hangisini yapmaz]
- Ortak: [kimler kullanır, erişim nasıl açılır]
- Denetlenen: [kim izler, hangi sıklıkla]

## 2. Görev tanımı

[İşin bugün nasıl yapıldığını üç cümleyle yaz. Fabrika hangi çıktıyı üretir?]

## 3. Tetikleyiciler

- Zamanlanmış: [örnek: her hafta pazartesi 09:00]
- Olay bazlı: {trigger}

## 4. Girdi, aşama ve çıktı

- Girdiler: [hangi veritabanları, dosyalar, sistemler]
- Aşamalar: {stages}
- Son çıktılar: [nereye kaydedilir, hangi kart güncellenir]

## 5. Araç ve erişim

- Gerekli erişim: {tools}
- Erişim vermeyelim: [açıkça yasak alanlar: gizli veri, üretim değişikliği, parasal işlem]

## 6. Gölge çalıştırma planı

1. İlk 5 çalıştırma tamamen taslak modda: gerçek eylem yok, sadece ne yapacağını raporla.
2. İnsan gözden geçirmesi: [kim, hangi ölçütle bakacak]
3. Geçiş kuralı: [kaç başarılı gölge çalıştırmadan sonra hacim artar]

## 7. Hacim planı

- Başlangıç hacmi: [örnek: günde 5 kart ya da %1]
- Artış kuralı: [hata oranı hangi eşikteyse hacim artar/geri çekilir]

## 8. Eval seti

| Görev | Yargı ölçütleri | Yargıç (kod / AI / insan) |
|-------|-----------------|---------------------------|
| [test görevi 1] | [doğru olması gerekenler] | [kim ya da ne karar verir] |
| [test görevi 2] | | |

## 9. İstem sürümleme

- İstemler nerede saklanır: [Prompt Versions veritabanı / sürüm kontrolü]
- Durum değerleri: testing, production, retired
- Geri dönüş kuralı: [yeni sürüm hangi koşulda geri çekilir]

## 10. Bağlam sistemi bağlantıları

- Kullanılacak çekirdek veritabanları: [Projeler, Görevler, Dokümanlar, Kişiler, Ekipler, Müşteriler]
- Yeni veritabanı önerisi: [{name} görev kartları + çalıştırma geçmişi]
- Bağlam çürümesi kontrolü: [hangi bilgiler ne sıklıkla bayatlık için taranır]
"""


def cmd_blueprint(args):
    stages = ", ".join(s.strip() for s in args.stages.split(",") if s.strip()) if args.stages else "teke bölünmemiş tek aşama"
    tools = args.tools or "[ajan için gerekli araçlar]"
    body = BLUEPRINT.format(name=args.name, trigger=args.trigger or "[tetikleyici belirtilmedi]", stages=stages, tools=tools)
    if args.out:
        Path(args.out).write_text(body, encoding="utf-8")
        print(f"Plan iskeleti yazıldı: {args.out}")
    else:
        print(body)
    return 0


def main():
    ap = argparse.ArgumentParser(description="AI fabrika adayı puanlayıcı ve plan iskeleti üretici")
    sub = ap.add_subparsers(dest="cmd", required=True)

    ck = sub.add_parser("check", help="adayı yedi nitelik üzerinden puanla")
    ck.add_argument("--name", required=True)
    ck.add_argument("--describe", help="serbest metin; eksik nitelikler bundan tahmin edilir")
    for key, _ in TRAITS:
        ck.add_argument(f"--{key}", help=f"evet/hayır (varsayılan: tahmin ya da hayır)")

    bp = sub.add_parser("blueprint", help="dört adımlı plan iskeleti üret")
    bp.add_argument("--name", required=True)
    bp.add_argument("--trigger", help="olay bazlı tetikleyici açıklaması")
    bp.add_argument("--stages", help="virgülle ayrılmış aşamalar")
    bp.add_argument("--tools", help="ajanın erişeceği araç ve sistemler")
    bp.add_argument("--out", help="çıktı dosyası (yoksa ekrana yazar)")

    args = ap.parse_args()
    if args.cmd == "check":
        sys.exit(cmd_check(args))
    if args.cmd == "blueprint":
        sys.exit(cmd_blueprint(args))


if __name__ == "__main__":
    main()
