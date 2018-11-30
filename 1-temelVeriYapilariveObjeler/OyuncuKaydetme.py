
print("Oyuncu kaydetme programi")

ad = input("Oyuncunun adini giriniz:")
soyad= input ("oyuncunun soyadini giriniz:")
takim= input("oyuncunun takimini giriniz:")

list = [ad,soyad,takim]

print("Bilgiler kaydediliyor...")

print("ad:{} \nsoyadi:{} \ntakimi: \n{}".format(list[0],list[1],list[2]))

print("Bilgiler kaydedildi")