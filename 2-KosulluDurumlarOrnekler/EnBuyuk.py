

print("En buyuk sayiyi bulma programi.")

a = int(input("Birinci Sayiyi Giriniz:"))
b = int(input("Ikinci Sayiyi Giriniz:"))
c = int(input("Ucuncu Sayiyi Giriniz:"))

if(a>=b and a>=c):
    print("En buyuk sayi:{}".format(a))
elif(b>=c and b>=a):
    print("En buyuk sayi:{}".format(b))
else:
    print("En buyuk sayi:{}".format(c))






