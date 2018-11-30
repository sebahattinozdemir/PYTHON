

print("""
***********************
Kullanici Giris Programi

***********************
""")

sys_kullanici_adi = "sebahattin"
sys_kullanici_parola = 12345

kullaniciAdi = input("Kullanici adini girniz:")
kullaniciParola = int(input("Parolanizi girniz:"))

if(sys_kullanici_adi == kullaniciAdi and sys_kullanici_parola == kullaniciParola):
    print("basarili bir sekilde giris yaptiniz.")

elif(sys_kullanici_parola != kullaniciParola and sys_kullanici_adi == kullaniciAdi):
    print("parolanizi kontrol edin.")

elif(sys_kullanici_adi != kullaniciAdi and sys_kullanici_parola == kullaniciParola):
    print("kullanici adinizi kontrol edin.")

else:
    print("kullanici adiniz ve parolaniz hatali!!")



