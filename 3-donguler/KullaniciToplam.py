
toplam=0
while True:
    sayi = input("Sayi:")
    if(sayi=="q"):
        print("Programdan Cikiliyor")
        break
    else:
        toplam += int(sayi)

print("Toplam:{}".format(toplam))