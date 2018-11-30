
print("*******Harf Notu hesaplama programina hosgeldiniz*******")


vize1 = int(input("Birinci vize notunuzu giriniz:"))
vize2 = int(input("Ikinci vize notunuzu giriniz:"))
final = int(input("Final notunuzu giriniz:"))

notunuz = vize1*0.3 + vize2*0.3 + final*0.4

if(notunuz>=90):
    print("Toplam Not :{}====> AA".format(notunuz))
elif(notunuz<90 and notunuz >=85):
        print("Toplam Not :{}====> BA".format(notunuz))
elif(notunuz<85 and notunuz >=80):
        print("Toplam Not :{}====> BB".format(notunuz))
elif(notunuz<80 and notunuz >=75):
        print("Toplam Not :{}====> CB".format(notunuz))
elif(notunuz<75 and notunuz >=70):
        print("Toplam Not :{}====> CC".format(notunuz))
elif(notunuz<70 and notunuz >=65):
        print("Toplam Not :{}====> DC".format(notunuz))
elif(notunuz<65 and notunuz >=60):
        print("Toplam Not :{}====> DD".format(notunuz))
else:
    print("Toplam Not :{}====> FF".format(notunuz))
