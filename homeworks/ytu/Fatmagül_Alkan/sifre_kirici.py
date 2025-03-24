#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 00:41:02 2025

@author: frosealkan
"""

def harfkaydir(harf,kaydirma_miktari):
    if'a' <= harf<='z': 
        return chr((ord(harf)-ord('a')+kaydirma_miktari) %26+ord('a'))
    elif'A'<= harf <='Z':
        return chr((ord(harf)-ord('A') +kaydirma_miktari) %26+ord('A'))
    return harf

def sayiterscevir(mesaj):
    yenimetin = ""
    gecicisayi = ""
    for karakter in mesaj:
        if karakter.isdigit():  
            gecicisayi +=karakter
        else:
            if gecicisayi: 
                yenimetin +=gecicisayi[::-1]
                gecicisayi = ""  
            yenimetin +=karakter  
    if gecicisayi:  
        yenimetin+= gecicisayi[::-1]
    return yenimetin

def sifre_coz(mesaj):
    mesaj = sayiterscevir(mesaj) 
    return "".join(harfkaydir(harf, -5) for harf in mesaj) 

def sifrele(mesaj):
    mesaj = sayiterscevir(mesaj) 
    return "".join(harfkaydir(harf, 5) for harf in mesaj) 

if __name__ == "__main__":
    sifrelimesaj = "ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl"
    cozulmus_mesaj = sifre_coz(sifrelimesaj)
    
    print("Şifreli Mesaj:", sifrelimesaj)
    print("Çözülen Mesaj:", cozulmus_mesaj)

    kullanici_mesaj = input("Şifrelemek istediğiniz mesajı girin: ")
    sifrelenmis = sifrele(kullanici_mesaj)
    print("Şifrelenmiş Hali:", sifrelenmis)