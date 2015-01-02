# -*- coding: cp1254 -*-
u"""Sezar Şifreleme Modülü
 _   __                   ___                  
| | / /                  / _ \                 
| |/ /  __ _ _ __ __ _  / /_\ \_   _  __ _ ____
|    \ / _` | '__/ _` | |  _  | | | |/ _` |_  /
| |\  \ (_| | | | (_| | | | | | |_| | (_| |/ / 
\_| \_/\__,_|_|  \__,_| \_| |_/\__, |\__,_/___|
                                __/ |          
                               |___/
Sezar Şifreleme ve Şifre Çözme Modülü | karaayaz_"""

def sifrele(veri):
    def ascii_a(x):
        return ord(x)+3
 
    def ascii_sc(x):
        return chr(x)
    
    sifreli_veri = list(map(ascii_a,veri))
    str(sifreli_veri[:-1])[1:-1]
    sifreli_metin = ''.join(ascii_sc(i) for i in sifreli_veri)
    return str(sifreli_metin)


def sifre_coz(veri):
    def ascii_e(x):
        return ord(x)-3
    
    def ascii_nc(x):
        return chr(x)

    normal_veri = list(map(ascii_e,veri))
    str(normal_veri[:-1])[1:-1]
    normal_metin = ''.join(ascii_nc(i) for i in normal_veri)
    return str(normal_metin)

def bilgi():
    print """"import sezar" diyerek sifreleme modulu yuklenir."""
    print """Kesinlikl Turkce karakter kullannilmaz"""
    print """Kullanilabilir fonksiyonlar;"""
    print """Fonksiyonlar;"""
    print """1) sifrele()"""
    print """    --> degisken = sezar.sifrele("sifrelenecekveri")"""
    print """2) sifre_coz()"""
    print """    --> degisken = sezar.sifre_coz("cozulecekveri")"""
