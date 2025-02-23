def asal_mi(sayi):
    if(sayi == 1 or sayi == 0):
        return False
    elif(sayi == 2):
        return True
    else:
        for i in range(2,sayi):
            if(sayi % i == 0):
                return False
        return True

while True:
    print("Cikis icin 'q' basiniz")
    sayi = input("Sayi: ")

    if(sayi == "q"):
        break
    else:
        sayi = int(sayi)

        if(asal_mi(sayi)):
            print(sayi, "asal sayidir.")
        else:
            print(sayi, "asal sayi degildir.")