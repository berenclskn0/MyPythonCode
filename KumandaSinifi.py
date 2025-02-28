import random
import time

class Kumanda():

    def __init__(self, tvDurum = "Kapali", tvSes = 0,kanalLsitesi = ["Now", "Show"], kanal = "Now"):
        self.tvDurum = tvDurum
        self.tvSes = tvSes
        self.kanalListesi = kanalLsitesi
        self.kanal = kanal

    def tvAc(self):
        if(self.tvDurum == "Acik"):
            print("Televizyon zaten acik")
        else:
            print("Televizyon aciliyor")
            self.tvDurum = "Acik"

    def tvKapat(self):
        if(self.tvDurum == "Kapali"):
            print("Televiyon zaten kapali")
        else:
            print("Teleziyon kapaniyor")
            self.tvDurum = "Kapali"

    def sesAyarlari(self):
        while True:
            cevap = input("Sesi azalt: '<'\nSesi arttir: '>'\nCikis: cikis")

            if cevap == "<":
                if(self.tvSes != 0):
                    self.tvSes -= 1
                    print("Ses: ", self.tvSes)

            elif cevap == ">":
                if(self.tvSes != 31):
                    self.tvSes += 1
                    print("Ses: ", self.tvSes)

            else:
                print("Ses Guncellendi: ", self.tvSes)
                break

    def kanalEkle(self,kanalIsmi):
        print("Kanal ekleniyor")
        time.sleep(2)
        self.kanalListesi.append(kanalIsmi)
        print("Kanal eklendi")

    def rastgeleKanal(self):
        rastgele = random.randint(0, len(self.kanalListesi) - 1)
        self.kanal = self.kanalListesi(rastgele)
        print("Su anki kanal: ", self.kanal)

    def __len__(self):
        return self.kanalListesi

    def __str__(self):
        return "Tv Durumu: {}\nTv Ses: {}\nKanal Listesi: {}\nSu anki kanal: {}".format(self.tvDurum, self.tvSes, self.kanalListesi, self.kanal)

kumanda = Kumanda()

print("""
Televizyon Uygulamasi

1.Tv Ac
2.Tv Kapat
3.Ses Ayarlari
4.Kanal Ekle
5.Kanal sayisini ogrenme
6.Rastgele kanal gecme
7.Televizyon Bilgileri
Cikmak icin 'q' basiniz

""")

while True:

    islem = input("Islem seciniz: ")

    if(islem == "q"):
        print("Program sonlandiriliyor")
        break

    elif islem == "1":
        kumanda.tvAc()
    elif islem == "2":
        kumanda.tvKapat()
    elif islem == "3":
        kumanda.sesAyarlari()
    elif islem == "4":
        kanalIsimleri = input("kanal isimlerini ',' ile ayirarak giriniz: ")
        kanalListesi = kanalIsimleri.split(",")

        for eklencekler in kanalListesi:
            kumanda.kanalEkle(eklencekler)
    elif islem == "5":
        print("Kanal sayisi: ", len(kumanda))
    elif islem == "6":
        kumanda.rastgeleKanal()
    elif islem == "7":
        print(kumanda)
    else:
        print("Gecersiz islem")