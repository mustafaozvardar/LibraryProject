from liste import *

kitap=Kitaplar()
print("""
            *** KÜTÜPHANE EKRANI ***

    -->İşlemler:

    1-Kitapları göster
    2-Kitap ekle
    3-Kitap sil
    4-Baskıları ve Toplamlarını göster
    5-Kitap isimlerini göster
    6-Kitap sorgula
    7-Verileri güncelle

    ->Not: çıkıs için q ya basın..

    """)
while True:
    print("---------------------")
    islem=input("Kitap ekranı secim: ")
    if(islem=="q"):
        print("Çıkıs yapılıyor...")
        time.sleep(1)
        break
    elif(islem=="1"):
        kitap.kitaplarıgöster()
    elif(islem=="2"):
        kitap.kitapekle()
    elif(islem=="3"):
        isim=input("Silinecek isim: ")
        print("Kitap siliniyor...")
        time.sleep(2)
        kitap.kitapsil(isim)
        print("Kitap silindi..")
    elif(islem=="4"):
        kitap.baskılarıgöster()
        kitap.baskıtoplam()
    elif(islem=="5"):
        kitap.isimlerigöster()
    elif(islem=="6"):
        isim = input("Hangi kitabı istiyorsunuz? --> : ")
        print("Kitap sorgulanıyor...")
        time.sleep(2)
        print("***KİTAP BİLGİLERİ***")
        print("---------------------")
        kitap.kitapsorgula(isim)

    elif(islem=="7"):
        kitap.verigüncelle()
    else:
        print("Hatali secim..")

