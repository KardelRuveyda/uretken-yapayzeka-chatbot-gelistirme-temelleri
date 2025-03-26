import string

def sifre_coz(mesaj):
    alfabe = string.ascii_lowercase
    sifrelenmis_harfler = {alfabe[i]: alfabe[(i - 5) % 26] for i in range(26)}
    sifrelenmis_harfler.update({k.upper(): v.upper() for k, v in sifrelenmis_harfler.items()})
    
    cozulmus = "".join(sifrelenmis_harfler.get(char, char) for char in mesaj)
    return cozulmus

def sifrele(mesaj):
    alfabe = string.ascii_lowercase
    sifrelenmis_harfler = {alfabe[i]: alfabe[(i + 5) % 26] for i in range(26)}
    sifrelenmis_harfler.update({k.upper(): v.upper() for k, v in sifrelenmis_harfler.items()})
    
    sifreli_mesaj = "".join(sifrelenmis_harfler.get(char, char) for char in mesaj)
    return sifreli_mesaj

def sayi_ters_cevir(mesaj):
    return "".join(str(int(k))[::-1] if k.isdigit() else k for k in mesaj)

def sifrelenmis_mesaji_coz(mesaj):
    mesaj = sayi_ters_cevir(mesaj)
    return sifre_coz(mesaj)

def kullanici_sifreleme():
    secim = input("Mesajı şifrelemek için 's', çözmek için 'ç' girin: ")
    mesaj = input("Mesajınızı girin: ")
    
    if secim == 's':
        print("Şifrelenmiş mesaj:", sifrele(mesaj))
    elif secim == 'ç':
        print("Çözülmüş mesaj:", sifrelenmis_mesaji_coz(mesaj))
    else:
        print("Geçersiz giriş!")

# Örnek kullanım
yazili_mesaj = "ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl"
print("Çözülen mesaj:", sifrelenmis_mesaji_coz(yazili_mesaj))

# Kullanıcının mesajını şifreleyip çözmesi için çağrı
kullanici_sifreleme()
