# Proyek: Panel Status Perangkat Virtual (Konsol Bit Masking)
# Topik: Arsitektur Komputer dan Operasi Tingkat Bit (Bitwise & Masking)

DONANIMLAR = [
    "Güç (Power)",  # Bit 0 -> 1 << 0 (00000001)
    "Wi-Fi",  # Bit 1 -> 1 << 1 (00000010)
    "Bluetooth",  # Bit 2 -> 1 << 2 (00000100)
    "Kamera",  # Bit 3 -> 1 << 3 (00001000)
    "Mikrofon",  # Bit 4 -> 1 << 4 (00010000)
    "GPS",  # Bit 5 -> 1 << 5 (00100000)
    "Hoparlör",  # Bit 6 -> 1 << 6 (01000000)
    "Fan (Soğutma)",  # Bit 7 -> 1 << 7 (10000000)
]


def durum_paneli_goster(status_register: int) -> None:
  """Menampilkan nilai Status Register 8-bit ke layar dalam bentuk tabel dan kotak bit."""
  binary_str = f"{status_register:08b}"

  print("\n" + "=" * 66)
  print("                 SANAL DONANIM DURUM PANELİ (8-BIT)")
  print("=" * 66)
  print(f"Register (Decimal): {status_register} | Hex: 0x{status_register:02X}")
  print(f"Register (Binary) : {binary_str}")
  print("-" * 66)

  # Tampilan kotak sel bit dari Bit 7 (kiri) ke Bit 0 (kanan)
  print("Bit No   : |  7  |  6  |  5  |  4  |  3  |  2  |  1  |  0  |")
  bit_kutulari = " | ".join(f" {bit} " for bit in binary_str)
  print(f"Bit Değ. : | {bit_kutulari} |")
  print("-" * 66)

  # Mengecek dan menampilkan status masing-masing perangkat keras
  for bit_no, isim in enumerate(DONANIMLAR):
    mask = 1 << bit_no
    aktif_mi = (
        status_register & mask
    ) != 0  # Mengecek apakah bit aktif menggunakan Bitwise AND
    durum_etiketi = "[ AÇIK (1) ]" if aktif_mi else "[ KAPALI (0) ]"
    print(f"Bit {bit_no} ({mask:3d} / 0b{mask:08b}) -> {isim:<16} : {durum_etiketi}")
  print("=" * 66)


def bit_sec() -> int | None:
  """Mengambil nomor bit/perangkat yang valid (0-7) dari input pengguna."""
  print("\nDonanım Listesi:")
  for i, isim in enumerate(DONANIMLAR):
    print(f"  {i} -> {isim}")

  secim = input("İşlem yapılacak Bit Numarasını girin (0-7): ").strip()
  if secim.isdigit() and 0 <= int(secim) <= 7:
    return int(secim)
  print("\n[HATA] Lütfen 0 ile 7 arasında geçerli bir sayı girin!")
  return None


def main() -> None:
  # Di awal program, seluruh perangkat dalam kondisi mati/nonaktif (00000000)
  status_register = 0b00000000

  durum_paneli_goster(status_register)

  while True:
    print("\n--- KONTROL MENÜSÜ ---")
    print("1- Durumları Gör")
    print("2- Bir Özelliği Aç (Bitwise OR: |)")
    print("3- Bir Özelliği Kapat (Bitwise AND & NOT: & ~)")
    print("4- Bir Özelliği Tersine Çevir / Toggle (Bitwise XOR: ^)")
    print("0- Çıkış")

    secim = input("\nSeçiminiz: ").strip()

    if secim == "1":
      durum_paneli_goster(status_register)

    elif secim == "2":
      bit = bit_sec()
      if bit is not None:
        mask = 1 << bit
        onceki = status_register
        status_register |= mask  # Mengubah bit terkait menjadi 1 (SET)
        print(
            f"\n[İŞLEM] {DONANIMLAR[bit]} AÇILDI -> "
            f"0b{onceki:08b} | 0b{mask:08b} = 0b{status_register:08b}"
        )
        durum_paneli_goster(status_register)

    elif secim == "3":
      bit = bit_sec()
      if bit is not None:
        mask = 1 << bit
        onceki = status_register
        status_register &= ~mask  # Mengubah bit terkait menjadi 0 (CLEAR)
        print(
            f"\n[İŞLEM] {DONANIMLAR[bit]} KAPATILDI -> "
            f"0b{onceki:08b} & ~(0b{mask:08b}) = 0b{status_register:08b}"
        )
        durum_paneli_goster(status_register)

    elif secim == "4":
      bit = bit_sec()
      if bit is not None:
        mask = 1 << bit
        onceki = status_register
        status_register ^= mask  # Membalikkan nilai bit terkait (TOGGLE)
        print(
            f"\n[İŞLEM] {DONANIMLAR[bit]} TERSİNE ÇEVRİLDİ -> "
            f"0b{onceki:08b} ^ 0b{mask:08b} = 0b{status_register:08b}"
        )
        durum_paneli_goster(status_register)

    elif secim == "0":
      print("\nSimülatörden çıkılıyor. İyi günler!")
      break

    else:
      print("\n[UYARI] Geçersiz seçim! Lütfen 0-4 arası bir değer girin.")


if __name__ == "__main__":
  main()