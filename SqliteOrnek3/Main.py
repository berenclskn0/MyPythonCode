from Supermarket import *

print("""
*************************************

Supermarket Programina Hosgeldiniz

Islemler;

1. Urun Goster

2. Urun Sorgula

3. Urun Ekle

4. Urun Sil

5. Kategoriye Gore Listele

Cikmak icin 'q' ya basiniz.

*************************************
""")

supermarket = Supermarket()

while True:
    islem = input("Yapmak istediginiz islem: ")

    if islem == "q":
        print("Program Sonlandiriliyor...")
        break

    elif islem == "1":
        supermarket.urunleri_goster()

    elif islem == "2":
        isim = input("Lutfen Urun Ismi Giriniz: ")
        supermarket.urun_sorgula(isim)

    elif islem == "3":
        isim = input("Isim: ")
        kategori = input("Kategori: ")
        uretici = input("Uretici: ")
        adet = int(input("Urun Adeti: "))
        fiyat = float(input("Urun Fiyat: "))

        yeni_urun = Urun(isim, kategori, uretici, adet, fiyat)

        supermarket.urun_ekle(yeni_urun)
        print("Urun Eklendi...")

    elif islem == "4":
        isim = input("Lutfen Silmek Istediginiz Urunun Ismini Giriniz: ")
        supermarket.urun_sil(isim)
        print("Urun Silindi...")

    elif islem == "5":
        kategori = input("Kategori: ")
        supermarket.kategoriye_gore_listele(kategori)