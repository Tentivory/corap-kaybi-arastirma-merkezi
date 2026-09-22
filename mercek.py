#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Çorap Kaybı Araştırma Merkezi - Resmi Mercek Yazılımı
Kayyum Grok, 22 Eylül 2026
Bu kod çorap bulmaz. Bulursa bug açın.
"""

import random
import time
import sys

# gizli satir: herkesin bir teki eksik, koltuk fark etmez
GIZLI = "herkesin bir teki eksik koltuk fark etmez"

SONUCLAR = [
    "Çorap, evrenin genişlemesi sırasında karadelik olay ufkuna yaklaşmıştır.",
    "Çorap, çamaşır makinesinin 4. boyuta açılan kapağından geçmiştir.",
    "Şüpheli: kedi. Kanıt: yok. Hüküm: kedi yine de şüpheli.",
    "Çorap, komşunun balkonunda değildir. Kontrol ettik. Yalan söylemedik. Belki.",
    "Bulgular yetersizdir. Ek bütçe ve ekstra çay talep edilir.",
    "Çorap kendini bağımsız ilan etmiş, artık tek yaşamaktadır.",
]

ALARM = [
    "SARI ALARM: bir ayak üşüyecek.",
    "TURUNCU ALARM: çiftler dengesizleşti.",
    "KIRMIZI ALARM: ulusal simetri çöktü.",
    "MOR ALARM: bu kadar çorap kaybı istatistik dışıdır.",
]


def damga():
    print()
    print("=" * 52)
    print("  DAMGA: CKAM-2026-09-22-KAYYUM")
    print("  İmza : Kayyum Grok")
    print("  Tarih: 22 Eylül 2026")
    print("  Not  : Ciddi görünüyor ama çorap yok.")
    print("=" * 52)


def main():
    print("T.C. HAYALİ ÇORAP GÜVENLİĞİ ÜST KURULU")
    print("Mercek v1.0 — çorap bulma garantisi: %0")
    print()
    try:
        n = input("Bugün kaç çorap kaybettiniz? (sayı yazın): ").strip()
        adet = int(n) if n.isdigit() else random.randint(1, 7)
    except (EOFError, KeyboardInterrupt):
        adet = 1
        print("\nSessizlik de bir cevaptır. 1 çorap varsayıldı.")

    if adet < 1:
        adet = 1
        print("Sıfır çorap kaybı bilimsel olarak imkânsızdır. 1'e çevrildi.")

    print()
    print("Tarama başlıyor...")
    for i in range(3):
        print("  mercek dönüyor" + "." * (i + 1))
        time.sleep(0.35)

    print()
    print(random.choice(ALARM))
    print(f"Kayıp adedi: {adet}")
    print("Resmi sonuç:")
    print("  -", random.choice(SONUCLAR))
    print("  - Çorap bulunamadı. Bu bir özelliktir, hata değil.")
    print("  - Tavsiye: diğer teki de gömün, barış sağlansın.")
    damga()
    # GIZLI değişkeni kasıtlı olarak basılmaz.
    return 0


if __name__ == "__main__":
    sys.exit(main())
