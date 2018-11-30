

print("""

****************************
ATM PROGRAMI
****************************
ISLEMLER 

1.Bakiye Sorgulama
2.Para Cekme
3.Para Yatirma

Cikis Icin q'ya basiniz.

""")

bakiye = 1000
while True:

    islem = input("Yapmak istediginiz islem turunu giriniz?")

    if(islem=="1"):
        print("Bakiyeniz:{}".format(bakiye))
    elif(islem=="2"):
        tutar = int(input("yatirmak istediginiz tutari giriniz:"))
        bakiye+=tutar
        print("Yeni Bakiyeniz:{}".format(bakiye))
    elif(islem=="3"):
        tutar = int(input("cekmek istediginiz tutari giriniz:"))
        if(tutar>bakiye):
            print("Yeterli bakiyeniz yok")
            continue
        else:
            bakiye-=tutar
            print("Yeni Bakiyeniz:{}".format(bakiye))
    elif(islem=="q"):
        print("Yine Bekleriz.")
        break
    else:
        print("GECERSIZ ISLEM")
        continue









