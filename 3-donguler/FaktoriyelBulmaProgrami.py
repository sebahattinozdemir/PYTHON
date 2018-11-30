

print("""

*****************************

Faktoriyel Bulma Programi

Cikis icin q'ya basiniz.

*****************************

""")

while True:

    sayi = input("Sayi=")

    if(sayi=="q"):
        print("Programdan cikiliyor...")
        break
    else:
        sayi = int(sayi)
        faktoriyel=1
        for i in range(2,sayi+1):
            faktoriyel*=i
            print("Faktoriyel:{} i:{}".format(faktoriyel, i))
    print("Faktoriyel:{}".format(faktoriyel))

