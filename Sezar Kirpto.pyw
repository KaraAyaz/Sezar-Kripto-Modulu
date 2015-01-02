# -*- coding: cp1254 -*-
import sezar, time
from Tkinter import*
anapen = Tk()


"""Sezar Şifreleme
 _   __                   ___                  
| | / /                  / _ \                 
| |/ /  __ _ _ __ __ _  / /_\ \_   _  __ _ ____
|    \ / _` | '__/ _` | |  _  | | | |/ _` |_  /
| |\  \ (_| | | | (_| | | | | | |_| | (_| |/ / 
\_| \_/\__,_|_|  \__,_| \_| |_/\__, |\__,_/___|
                                __/ |          
                               |___/
Sezar Şifreleme ve Şifre Çözme Programı | karaayaz_"""



#Pencere Özellikleri
anapen.title(u"Sezar Şifreleme & Şifre Çözme")
anapen.geometry("480x400+300+100")
anapen.wm_iconbitmap("gray12")
anapen.resizable(False, False)
anapen.wm_attributes("-topmost", 1)
anapen.tk_setPalette("black")

#Sabitler
kullanici = ("Kara Ayaz","PyCoder")
denemeHakki = 3
zaman = 0

def GirisYap():
    global denemeHakki, zaman
    if denemeHakki <=0:
        if time.time()-zaman >= 900:
            denemeHakki = 3
        else:
            sonuc.config(text = u"15 dk Beklemeniz Gerekiyor")
            return False
    username = kadi.get()
    password = passw.get()
    if username == kullanici[0] and password == kullanici[1]:
        sonuc.config(text = u"Başarıyla Giriş Yapıldı")
        Kullanici_Karsila()
    else:
        denemeHakki -= 1
        if denemeHakki == 0:
            zaman = time.time()
        sonuc.config(text = u"Bilgiler Yanlış! Deneme: {}".format(denemeHakki))

def Kullanici_Karsila():
    def sifre_olustur():
        a_veri = giris.get(0.0, END)
        s_veri = sezar.sifrele(a_veri)
        cikis.delete(0.0,END)
        cikis.insert(INSERT, s_veri)
    def sifre_coz():
        a_veri = giris.get(0.0, END)
        s_veri = sezar.sifre_coz(a_veri)
        cikis.delete(0.0,END)
        cikis.insert(INSERT, s_veri)

    karsila = Label(anapen)
    karsila.config(text=u"Sayın {}, Hoş Geldiniz.".format(kullanici[0]))
    karsila.place(x=1,y=1)

    GirisBir = Label(anapen)
    GirisBir.config(text=u"Giriş:")
    GirisBir.place(x=1, y=25)

    giris = Text(anapen)
    giris.config(width = 40, height = 8, font = "arial 12")
    giris.place(x=100, y=25)

    CikisBir = Label(anapen)
    CikisBir.config(text=u"Çıkış:")
    CikisBir.place(x=1, y=200)

    cikis = Text(anapen)
    cikis.config(width = 40, height = 8, font = "arial 12")
    cikis.place(x=100, y=200)

    Sifrele = Button(anapen)
    Sifrele.config(text=u"Şifrele!", command=sifre_olustur)
    Sifrele.place(x=100, y=355)

    Coz = Button(anapen)
    Coz.config(text = u"Şifre Çöz!", command=sifre_coz)
    Coz.place(x=405, y=355)

    g_karsila.destroy()
    kadi_sor.destroy()
    kadi.destroy()
    passw_sor.destroy()
    passw.destroy()
    g_buton.destroy()
    sonuc.destroy()


g_karsila = Label(anapen)
g_karsila.config(text=u"Sezar Şifreleme Programı")
g_karsila.place(x=1, y=1)


kadi_sor = Label(anapen)
kadi_sor.config(text = u"Kullanıcı Adı:")
kadi_sor.place(x=1,y=25)

kadi = Entry(anapen)
kadi.place(x=150,y=25)

passw_sor = Label(anapen)
passw_sor.config(text = u"Kullanıcı Şifre:")
passw_sor.place(x=1,y=50)

passw = Entry(anapen)
passw.place(x=150,y=50)

g_buton = Button(anapen)
g_buton.config(text = u"Giriş", command=GirisYap)
g_buton.place(x=300,y=45)

sonuc = Label(anapen)
sonuc.config(text = u"Henüz işlem yapılmadı")
sonuc.place(x=300,y=20)


ayaz = Label(anapen)
ayaz.config(text="""Coder: Kara Ayaz\tskype: karaayaz_""")
ayaz.place(x=1, y=100)

mainloop()
