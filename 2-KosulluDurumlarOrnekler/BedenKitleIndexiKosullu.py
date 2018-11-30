

print("Beden Kitle Indexi Programinia hosgeldiniz:")

kilo = float(input("Kilonuzu giriniz:"))
boy = float(input("Boyunuzu giriniz:"))

bedenKitleIndexi = kilo/(boy*boy)

if(bedenKitleIndexi<18.5):
    print("Zayifsiniz.Beden Kitle Indexiniz{}".format(bedenKitleIndexi))
elif(bedenKitleIndexi>=18.5 and bedenKitleIndexi<25):
    print("Normal.{}".format(bedenKitleIndexi))
elif(bedenKitleIndexi>=25 and bedenKitleIndexi<30):
    print("Fazla Kilolu.{}".format(bedenKitleIndexi))
else:
    print("Obez.{}".format(bedenKitleIndexi))

