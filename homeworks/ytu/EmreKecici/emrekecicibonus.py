metin = input("Şifrelemek istediğiniz metni girin: ")

sifre = ""
sayi = ""

# Şifreleme
for karakter in metin:
    if karakter >= 'a' and karakter <= 'z':
        if sayi != "":
            sifre += sayi[::-1]
            sayi = ""
        kod = ord(karakter) + 5
        if kod > ord('z'):
            kod = kod - 26
        sifre += chr(kod)
    elif karakter >= '0' and karakter <= '9':
        sayi += karakter
    else:
        if sayi != "":
            sifre += sayi[::-1]
            sayi = ""
        sifre += karakter

if sayi != "":
    sifre += sayi[::-1]

print("Şifrelenmiş metin:", sifre)

# Şifreyi geri açmak için
secim = input("Şifreyi geri açmak için X'e basın: ")

if secim == "X" or secim == "x":
    cozulmus = ""
    sayi2 = ""

    for harf in sifre:
        if harf >= 'a' and harf <= 'z':
            if sayi2 != "":
                cozulmus += sayi2[::-1]
                sayi2 = ""
            kod = ord(harf) - 5
            if kod < ord('a'):
                kod += 26
            cozulmus += chr(kod)
        elif harf >= '0' and harf <= '9':
            sayi2 += harf
        else:
            if sayi2 != "":
                cozulmus += sayi2[::-1]
                sayi2 = ""
            cozulmus += harf

    if sayi2 != "":
        cozulmus += sayi2[::-1]

    print("Çözülmüş metin:", cozulmus)
