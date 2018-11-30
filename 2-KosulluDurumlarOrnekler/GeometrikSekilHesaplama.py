

print("***Geometrik Sekil Bulma Programina Hosgeldiniz***")

answ = input("Hangi sekli bulmak istiyorsunuz:(ucgen or dortgen)")

if(answ == "dortgen"):
    a = int(input("Birinci Kenar:"))
    b = int(input("Ikinci Kenar:"))
    c = int(input("Ucuncu Kenar:"))
    d = int(input("Dorduncu Kenar:"))
    if( a == b and a == c and a == d):
        print("Bu bir karedir.")
    elif(a == c and b == d):
        print("Bi bir dikdortgendir.")
    else:
        print("Siradan bir dikdortgen.")
elif(answ == "ucgen"):
    a = int(input("Birinci Kenar:"))
    b = int(input("Ikinci Kenar:"))
    c = int(input("Ucuncu Kenar:"))
    if ((abs(b - c) < a < b + c and abs(a - c) < b < a + c and abs(a - b) < c < a + b)):
        if(a==b and a==c and c==b):
            print("Eskenar ucgendir.")
        elif((a==b or a==c) or (b==c) ):
            print("Ikizkenar Ucgen.")
        else:
            print("Siradan bir ucgendir.")

    else:
        print("Bu bir ucgen degildir")
else:
    print("Gecersiz islem.")

