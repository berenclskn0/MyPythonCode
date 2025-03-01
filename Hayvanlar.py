class Hayvan:

    def __init__(self, isim, yas):
        self.isim = isim
        self.yas = yas

    def sesCikar(self):
        pass

    def __str__(self):
        return (f"Isim: {self.isim}\nYas: {self.yas}")

class Kopek(Hayvan):

    def __init__(self, isim, yas,cins):
        super().__init__(isim, yas)
        self.cins = cins

    def sesCikar(self):
        return "Hav Hav"

    def __str__(self):
        return super().__str__() + f"\nCins: {self.cins}"

class Kus(Hayvan):

    def __init__(self, isim, yas, kanatUzunlugu):
        super().__init__(isim, yas)
        self.kanatUzunlugu = kanatUzunlugu

    def sesCikar(self):
        return "Cik Cik"

    def __str__(self):
        return super().__str__() + f"\nKanat Uzunlugu: {self.kanatUzunlugu}"

class At (Hayvan):

    def __init__(self, isim, yas, hiz):
        super().__init__(isim, yas)
        self.hiz = hiz

    def sesCikar(self):
        return "ihahaa"

    def __str__(self):
        return super().__str__() + f"\nHiz: {self.hiz}"

print("*****************")
isim = input("Isim: ")
yas = int(input("Yas: "))
cins = input("Cins: ")
kopek = Kopek(isim, yas, cins)

print(kopek)
print("Ses: ", kopek.sesCikar())

print("*****************")

isim = input("Isim: ")
yas = int(input("Yas: "))
kanatUzunlugu = int(input("Kanat Uzunlugu: "))
kus = Kus(isim, yas, kanatUzunlugu)

print(kus)
print("Ses: ", kus.sesCikar())

print("*****************")

isim = input("Isim: ")
yas = int(input("Yas: "))
hiz = int(input("Hiz: "))
at = At(isim, yas, hiz)

print(at)
print("Ses: ", at.sesCikar())

print("*****************")