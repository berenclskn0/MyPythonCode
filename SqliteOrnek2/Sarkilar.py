import sqlite3

class Sarki():

    def __init__(self, sarkiIsmi, sanatciIsmi, albumIsmi, sirketIsmi, sarkiSuresi):

        self.sarkiIsmi = sarkiIsmi
        self.sanatciIsmi = sanatciIsmi
        self.albumIsmi = albumIsmi
        self.sirketIsmi = sirketIsmi
        self.sarkiSuresi = sarkiSuresi

    def __str__(self):

        return "Sarki: {}\nSanatci: {}\nAlbum: {}\nSirket: {}\nSarki Suresi: {}".format(self.sarkiIsmi, self.sanatciIsmi, self.albumIsmi, self.sirketIsmi, self.sarkiSuresi)

class Sarkilar():

    def __init__(self):

        self.baglanti_olustur()

    def baglanti_olustur(self):

        self.baglanti = sqlite3.connect("Sarkilar.db")
        self.cursor = self.baglanti.cursor()

        sorgu = "Create Table if not exists sarkilar(sarkiIsmi TEXT, sanatciIsmi TEXT, albumIsmi TEXT, sirketIsmi TEXT, sarkiSuresi INT)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()

    def baglantiyi_kes(self):
        self.baglanti.close()

    def sarkilari_goster(self):

        sorgu = "Select * from sarkilar"
        self.cursor.execute(sorgu)

        sarkilar = self.cursor.fetchall()

        if(len(sarkilar) == 0):
            print("Listenizde Sarki Bulunmuyor...")

        else:
            for i in sarkilar:
                sarki = Sarki(i[0], i[1], i[2], i[3], i[4])
                print(sarki)

    def sarki_sorgula(self, sarkiIsmi):

        sorgu = "Select * from sarkilar where sarkiIsmi = ?"
        self.cursor.execute(sorgu,(sarkiIsmi,))

        sarkilar = self.cursor.fetchall()

        if(len(sarkilar) == 0):
            print("Listenizde Boyle bir Sarki Bulunmuyor...")

        else:
            sarki = Sarki(sarkilar[0][0],sarkilar[0][1],sarkilar[0][2],sarkilar[0][3],sarkilar[0][4])
            print(sarki)

    def sarki_ekle(self, sarki):

        sorgu = "Insert into sarkilar Values (?,?,?,?,?)"
        self.cursor.execute(sorgu,(sarki.sarkiIsmi, sarki.sanatciIsmi, sarki.albumIsmi, sarki.sirketIsmi, sarki.sarkiSuresi))

        self.baglanti.commit()

    def sarki_sil(self, sarkiIsmi):

        sorgu = "Delete from sarkilar where sarkiIsmi = ?"
        self.cursor.execute(sorgu,(sarkiIsmi,))

        self.baglanti.commit()

    def toplam_sure_hesapla(self):

        sorgu = "Select Sum(sarkiSuresi) From sarkilar"
        self.cursor.execute(sorgu)
        toplam = self.cursor.fetchall()[0][0]

        if(toplam is None):
            print("Listenizde Sarki Bulunmuyor...")
        else:
            print(f"Toplam sarki suresi: {toplam} saniye")