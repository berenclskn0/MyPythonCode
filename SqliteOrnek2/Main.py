from Sarkilar import *

print("""
*************************************

Sarki Programina Hosgeldiniz

Islemler;

1. Sarki Goster

2. Sarki Sorgula

3. Sarki Ekle

4. Sarki Sil

5. Listenizdeki Toplam Sarki Suresi

Cikmak icin 'q' ya basiniz.

*************************************
""")

sarkilar = Sarkilar()

while True:
    islem = input("Yapmak istediginiz islem: ")

    if islem == "q":
        print("Program Sonlandiriliyor...")
        break

    elif islem == "1":
        sarkilar.sarkilari_goster()

    elif islem == "2":
        sarkiIsmi = input("Sarki Ismi: ")
        sarkilar.sarki_sorgula(sarkiIsmi)

    elif islem == "3":
        sarkiIsmi = input("Sarki Ismi: ")
        sanatciIsmi = input("Sanatci Ismi: ")
        albumIsmi = input("Album ismi: ")
        sirketIsmi = input("Sirket Ismi: ")
        sarkiSuresi = int(input("Sarki Suresi: "))

        yeni_sarki = Sarki(sarkiIsmi,sanatciIsmi,albumIsmi,sirketIsmi,sarkiSuresi)

        sarkilar.sarki_ekle(yeni_sarki)
        print("Sarki Listeye Eklendi...")

    elif islem == "4":
        sarkiIsmi = input("Lutfen Silmek Istediginiz Sarkinin Ismini Giriniz: ")

        sarkilar.sarki_sil(sarkiIsmi)
        print("Sarki Listeden Silindi...")

    elif islem == "5":
        sarkilar.toplam_sure_hesapla()