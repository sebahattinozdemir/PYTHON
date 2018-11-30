

def yazdir(sayi):

    birler = ["sifir","bir","iki","uc","dort","bes","alti","yedi","sekiz","dokuz"]
    onlar  =["","on","yirmi","otuz","kirk","elli","altmis","yetmis","seksen","doksan"]

    birlerbasamai = sayi%10

    onlarbasamagi = sayi//10

    print(onlar[onlarbasamagi],birler[birlerbasamai])


sayi = int(input("Sayi giriniz:"))
yazdir(sayi)