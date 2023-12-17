import sqlite3
import random
import time

con=sqlite3.connect("kütüphane.db")
cursor=con.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS kitaplar (isim TEXT,yazar TEXT,baskı INT)")

class Kitap():
    def __init__(self,isim,yazar,baskı):
        self.isim=isim
        self.yazar=yazar
        self.baskı=baskı

    def __str__(self):
        return "Kitap İsmi: {}\nYazar: {}\nBaskı: {}\n-----------------".format(self.isim,self.yazar,self.baskı)


class Kitaplar():
    def kitapekle(self):
        isim=input("Kitap ismi: ")
        yazar=input("Yazar: ")
        baskı=int(input("Baskı: "))
        print("Kitap ekleniyor....")
        time.sleep(2)
        cursor.execute("INSERT INTO kitaplar (isim,yazar,baskı) VALUES(?,?,?) ",[isim,yazar,baskı])
        con.commit()
        print("Kitap eklendi...")

    def kitapsil(self,isim):
        cursor.execute("DELETE FROM kitaplar WHERE isim=?",[isim])
        con.commit()

    def kitaplarıgöster(self):
        print("-------Kitap Bilgileri----------")
        cursor.execute("SELECT * FROM kitaplar")
        kitaplar=cursor.fetchall()
        if(len(kitaplar)==0):
            print("Kütüphane kitap bulunmuyor...")
        else:
            for i in kitaplar:
                kitap=Kitap(i[0],i[1],i[2])
                print(kitap)
        con.commit()

    def baskılarıgöster(self):
        print("---BASKI BİLGİLERİ---")
        cursor.execute("SELECT baskı FROM kitaplar")
        liste = cursor.fetchall()
        if (len(liste) == 0):
            print("kitap baskısı yok..")
        else:
            for i in range(len(liste)):
                print(i, ".ncı indeksin verisi -->: ", liste[i])


    def isimlerigöster(self):
        print("---KİTAP İSİMLERİ---")
        cursor.execute("SELECT isim FROM kitaplar")
        liste=cursor.fetchall()
        if(len(liste)==0):
            print("kitap ismi yok..")
        else:
            for i in range(len(liste)):
                print(i, ".ncı indeksin verisi -->: ", liste[i])

    def baskıtoplam(self):
        cursor.execute("SELECT * FROM kitaplar")
        liste=cursor.fetchall()
        süre=0
        for i in liste:
            süre=süre+i[2]
        print("toplam: ",süre)

    def verigüncelle(self):
        cursor.execute("SELECT * FROM kitaplar ")
        data=cursor.fetchall()
        print("------İLK DEGERLER------")
        for i in data:
            print(i)

        print("Güncellenicek satırı seçiniz\n1-İsim\t2-Yazar\t3-Baskı")
        print("-------------------------------------------------------")
        satır=input("Cevap: ")
        print("----------------------------------------------------")
        if(satır=="1"):
            yazar=input("Hangi yazarın kitabını güncelliyeceksiniz?: ")
            isim=input("Yeni kitap ismini girin: ")
            print("**Güncelleniyor.....")
            time.sleep(2)
            cursor.execute("UPDATE kitaplar SET isim=? WHERE yazar=?",[isim,yazar])
            cursor.execute("SELECT * FROM kitaplar")
            data=cursor.fetchall()
            print("----GÜNCEL HALİ-----")
            for i in data:
                print(i)

        elif(satır=="3"):
            yazar=input("Hangi yazarın baskını güncelliyeceksiniz?: ")
            baskı=int(input("Yeni baskı: "))
            print("**Güncelleniyor.....")
            time.sleep(2)
            cursor.execute("UPDATE kitaplar SET baskı=? WHERE yazar=?",[baskı,yazar])
            cursor.execute("SELECT * FROM kitaplar")
            data=cursor.fetchall()
            print("----GÜNCEL HALİ----")
            for i in data:
                print(i)

        elif(satır=="2"):
            yazar=input("Hangi yazarın kitabını güncelliyeceksiniz?: ")
            kitap=input("Yeni kitap: ")
            print("**Güncelleniyor.....")
            time.sleep(2)
            cursor.execute("UPDATE kitaplar SET isim=? WHERE yazar=?",[kitap,yazar])
            cursor.execute("SELECT * FROM kitaplar")
            data=cursor.fetchall()
            print("----GÜNCEL HALİ----")
            for i in data:
                print(i)


        else:
            print("hatali giriş..")
        con.commit()

    def kitapsorgula(self,isim):
        cursor.execute("SELECT * FROM kitaplar WHERE isim=?",[isim])
        kitaplar=cursor.fetchall()
        if(len(kitaplar)==0):
            print("Böyle bir kitap yok..!")
        else:
            kitap=Kitap(kitaplar[0][0],kitaplar[0][1],kitaplar[0][2])
            print(kitap)




    def vtkapat(self):
        con.close()