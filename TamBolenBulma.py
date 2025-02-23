def tambolenbulma(sayi):
    tam_bolen = []

    for i in range(2,sayi):
        if (sayi % i == 0):
            tam_bolen.append(i)
    return tam_bolen

while True:
    print("Cikis icin 'q' basiniz")
    sayi = input("Sayi: ")

    if(sayi == "q"):
        print("Program Sonlandiriliyor...")
        break
    else:
        sayi = int(sayi)
        print("Tam bolenler:",tambolenbulma(sayi))