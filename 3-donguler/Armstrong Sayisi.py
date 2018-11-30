

print("""
*********************
Armstrong Sayi mi Programi
*********************
""")

sayi = int(input("Sayi:"))

basamakSayisi = 0

i=0
temp=sayi

for i in range(temp):

    if sayi > 0:
        sayi//=10
        basamakSayisi+=1

sayi=temp
result = 0

for i in range(temp):

    if sayi > 0:
        basamak=sayi%10

        result += basamak ** basamakSayisi
        sayi//=10

sayi=temp

if(result == sayi):

    print("Bu bir armstrong sayisidir.")

print("Basamak Sayisi:{} Sonuc:{}".format(basamakSayisi,result))




