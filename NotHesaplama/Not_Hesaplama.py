def not_hesapla(satir):
    satir = satir[:-1]

    liste = satir.split(",")

    isim = liste[0]
    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])

    ort = not1 * 0.3 + not2 * 0.3 + not3 * 0.4

    if ort >= 90:
        harf = "AA"
    elif ort >= 85:
        harf = "BA"
    elif ort >= 80:
        harf = "BB"
    elif ort >= 75:
        harf = "BC"
    elif ort >= 70:
        harf = "CC"
    elif ort >= 65:
        harf = "DC"
    elif ort >= 60:
        harf = "DD"
    elif ort >= 55:
        harf = "FD"
    else:
        harf = "FF"

    return isim + "------>" + harf + "\n"

with open("notlar.txt","r", encoding="utf-8") as file:

    eklenecekler_listesi = []

    for i in file:
        eklenecekler_listesi.append(not_hesapla(i))

    with open("notlar2.txt","w", encoding="utf-8") as file2:

        for i in eklenecekler_listesi:
            file2.write(i)