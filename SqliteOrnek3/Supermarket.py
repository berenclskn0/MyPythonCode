import sqlite3

class Urun():

    def __init__(self,isim, kategori, uretici, adet, fiyat):
        self.isim = isim
        self.kategori = kategori
        self.uretici = uretici
        self.adet = adet
        self.fiyat = fiyat

    def __str__(self):
        return "Urun Ismi: {}\nKategori: {}\nUretici Firma: {}\nStok Sayisi: {}\nFiyati: {}".format(self.isim, self.kategori, self.uretici, self.adet, self.fiyat)

class Supermarket():

    def __init__(self):
        self.baglanti_olustur()

    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect('Supermarket.db')
        self.cursor = self.baglanti.cursor()

        sorgu = "Create Table if not exists urunler(isim TEXT, kategori TEXT, uretici TEXT, adet INT, fiyat FLOAT)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()

    def baglantiyi_kes(self):
        self.baglanti.close()

    def urunleri_goster(self):
        sorgu = "select * from urunler"
        self.cursor.execute(sorgu)
        urunler = self.cursor.fetchall()

        if (len(urunler) == 0):
            print("Supermarkette urun bulunmuyor")

        else:
            for i in urunler:
                urun = Urun(i[0], i[1], i[2], i[3], i[4])
                print(urun)

    def urun_sorgula(self, isim):
        sorgu = "select * from urunler Where isim = ?"
        self.cursor.execute(sorgu, (isim,))
        urunler = self.cursor.fetchall()

        if (len(urunler) == 0):
            print("Supermarkette boyle bir urun bulunmuyor")

        else:
            urun = Urun(urunler[0][0],urunler[0][1],urunler[0][2],urunler[0][3],urunler[0][4])
            print(urun)

    def urun_ekle(self, urun):
        sorgu = "Insert into urunler Values(?,?,?,?,?)"
        self.cursor.execute(sorgu, (urun.isim, urun.kategori, urun.uretici, urun.adet, urun.fiyat))
        self.baglanti.commit()

    def urun_sil(self, isim):
        sorgu = "Delete from urunler where isim = ?"
        self.cursor.execute(sorgu,(isim,))
        self.baglanti.commit()

    def kategoriye_gore_listele(self, kategori):
        sorgu = "select * from urunler Where kategori = ?"
        self.cursor.execute(sorgu, (kategori,))
        urunler = self.cursor.fetchall()

        if len(urunler) == 0:
            print(f"{kategori} kategorisinde ürün bulunamadı.")
        else:
            for i in urunler:
                urun = Urun(i[0], i[1], i[2], i[3], i[4])
                print(urun)