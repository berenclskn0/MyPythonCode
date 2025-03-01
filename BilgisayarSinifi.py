class Bilgisayar:

    def __init__(self,marka, model, islemci, ram, depolama, bilgisayarDurum = "Kapali"):
        self.marka = marka
        self.model = model
        self.islemci = islemci
        self.ram = ram
        self.depolama = depolama
        self.bilgisayarDurum = bilgisayarDurum

    def __len__(self):
        return self.ram + self.depolama

    def ac(self):
        if self.bilgisayarDurum == "Acik":
            print("Bilgisayar zaten acik.")
        else:
            print("Bilgisayar aciliyor...")
            self.bilgisayarDurum = "Acik"

    def kapat(self):
        if self.bilgisayarDurum == "Kapali":
            print("Bilgisayar zaten kapali.")
        else:
            print("Bilgisayar kapaniyor...")
            self.bilgisayarDurum = "Kapali"

    def bilgileriGoster(self):
        print(f"Marka: {self.marka}\nModel: {self.model}\nİşlemci: {self.islemci}\nRAM: {self.ram}GB\nDepolama: {self.depolama}GB\nDurum: {self.bilgisayarDurum}")

    def ramYukle(self, yeniRam):
        if yeniRam > self.ram:
            print(f"RAM {self.ram}GB'tan {yeniRam}GB'a yükseltildi.")
            self.ram = yeniRam
        else:
            print("Yeni RAM kapasitesi mevcut RAM'den düşük veya eşit olamaz!")

    def depolamaYukle(self, yeniDepolama):
        self.depolama += yeniDepolama
        print(f"Depolama {self.depolama - yeniDepolama}GB'tan {self.depolama}GB'a yükseltildi.")

    def isletimSistemiKur(self, sistem):
        self.islemci = sistem
        print(f"{self.marka} {self.model} bilgisayarına {sistem} işletim sistemi kuruldu.")

    def formatAt(self):
        print(f"{self.marka} {self.model} bilgasayara format atildi.")

marka = input("Marka giriniz: ")
model = input("Model giriniz: ")
islemci = input("Islemci giriniz: ")
ram = int(input("RAM giriniz: "))
depolama = int(input("Depolama giriniz: "))

pc1 = Bilgisayar(marka, model, islemci, ram, depolama)

print("""
Bilgisayar Islemleri

1.Toplam bilgisayar kapasitesini ogrenme
2.Bilgisayari acma
3.Bilgisayari kapatma
4.Bilgisayar bilgilerini goster
5.Bilgisayara yeni RAM yukleme
6.Bilgisayara yeni depolama alani yukleme
7.Bilgisayara format atma
Cikmak icin 'q' basiniz

""")
while True:

    islem = input("Islem seciniz: ")

    if islem == "q":
        print("Bilgisayardan cikiliyor...")
        break

    elif islem == "1":
        print(len(pc1))

    elif islem == "2":
        pc1.ac()

    elif islem == "3":
        pc1.kapat()

    elif islem == "4":
        pc1.bilgileriGoster()

    elif islem == "5":
        yeniRam = int(input("Yeni RAM kapasitesini giriniz: "))
        pc1.ramYukle(yeniRam)

    elif islem == "6":
        yeniDepolama = int(input("Yeni depolama alani giriniz: "))
        pc1.depolamaYukle(yeniDepolama)

    elif islem == "7":
        pc1.formatAt()

    else:
        print("Gecersiz islem girdiniz.")