

print("""
*******************
Perfect Number Bulma Programi(6) sayisinin bolenleri bulma 1+2+3 = 6
*******************
""")


sayi = int(input("Bir sayi giriniz:"))
toplam=0
for i in range(1,sayi) :

    if(sayi%i==0):
        toplam+=i
    else:
        continue
if(toplam==sayi):
    print("bu bir mukemmel sayidir.")
else:
    print("Mukemmel sayi degildir")




