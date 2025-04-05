#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 22:38:44 2025

@author: hamza
"""

import string

def şifreleme(metin):
    alfabe = string.ascii_lowercase
    şifreli_metin = ""
    
    for karakter in metin:
        if karakter.isalpha():
            kucuk_harf = karakter.lower()
            yeni_harf = alfabe[(alfabe.index(kucuk_harf) + 5) % 26]
            şifreli_metin += yeni_harf if karakter.islower() else yeni_harf.upper()
        elif karakter.isdigit():
            şifreli_metin = karakter + şifreli_metin
        else:
            şifreli_metin += karakter
    
    return şifreli_metin

def deşifreleme(şifreli_metin):
    alfabe = string.ascii_lowercase
    orijinal_metin = ""
    ters_çevrilen_sayılar = ""

    for karakter in şifreli_metin:
        if karakter.isalpha():
            küçük_harf = karakter.lower()
            yeni_harf = alfabe[(alfabe.index(küçük_harf) - 5) % 26]
            orijinal_metin += yeni_harf if karakter.islower() else yeni_harf.upper()
        elif karakter.isdigit():
            ters_çevrilen_sayılar = karakter + ters_çevrilen_sayılar
        else:
            orijinal_metin += karakter

    return orijinal_metin + ters_çevrilen_sayılar

while True:
    seçim = input("Şifreleme yapmak için '1', şifre çözmek için '2' yazın: ").strip()
    
    if seçim == "1":
        metin = input("Şifrelenecek metni girin: ")
        print("Şifreli Metin:", şifreleme(metin))
        break
    elif seçim == "2":
        şifreli_metin = input("Çözülecek şifreli metni girin: ")
        print("Çözülen Metin:", deşifreleme(şifreli_metin))
        break
    else:
        print("Geçersiz seçim! Lütfen 1 veya 2 girin.")
