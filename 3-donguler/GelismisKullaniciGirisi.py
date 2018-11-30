

print("""
***************************
Gelismis Kullanici Programi
***************************
""")

sysKullaniciAdi = "sebahattin"
sysParola = "123456"
girisHakki=3

while True:
    kullaniciAdi = input("Kullanici Adini Giriniz:")
    parola = input("Parolanizi Giriniz:")

    if(sysKullaniciAdi == kullaniciAdi and sysParola == parola):
        print("Basarili Bir sekilde giris yaptiniz. Tebrikler!!!")
        break
    elif(sysKullaniciAdi != kullaniciAdi and sysParola != parola):
        girisHakki -= 1
        print("Kullanici Adiniz ve Parolaniz Hatali!!! . Kalan Giris Hakki {}".format(girisHakki))
    elif(sysKullaniciAdi == kullaniciAdi and sysParola != parola):

        girisHakki -= 1
        print("Parolaniz hatali. Kalan Giris Hakki:{}".format(girisHakki))
    else :
        girisHakki -= 1
        print("Kullanici Adiniz Hatali. Kalan Giris Hakki:{}".format(girisHakki))
    if(girisHakki == 0):
        print("Giris Hakkiniz Bitti!!!")
        break