
print("""
Calculator App

********************************
Islemler

1. Toplama Islemi

2. Cikarma Islemi

3. Carpma Islemi

4. Bolme Islemi

5. Mod alma islemi
 
********************************
""")

a = int(input("Birinci Sayi:"))

b = int(input("Ikinci Sayi:"))

islem = input("Islemi giriniz:")

if(islem == "1"):
    print("{} ile {} nin toplami = {}".format(a, b, (a+b)))

elif(islem == "2"):
    print("{} ile {} nin farki = {}".format(a, b, (a-b)))

elif(islem == "3"):
    print("{} ile {} nin carpimi = {}".format(a,b,(a*b)))

elif(islem == "4"):
    print("{} ile {} nin bolumu = {}".format(a, b, (a/b)))

elif(islem == "5"):
    print("{} ile {} nin modu = {}".format(a, b, (a%b)))
else:
    print("Gecersiz islem...")
    