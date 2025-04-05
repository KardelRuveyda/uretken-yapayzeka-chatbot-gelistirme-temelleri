# şifreli metni çözülmüş metne çevirme

def sifre_coz(sifreli_metin):
    alfabe = "abcdefghijklmnopqrstuvwxyz"
    cozulmus_metin = ""
    for karakter in sifreli_metin:
        if karakter.lower() in alfabe:
            indeks = alfabe.find(karakter.lower())
            yeni_indeks = (indeks - 5) % 26 
            if karakter.isupper():
                cozulmus_metin += alfabe[yeni_indeks].upper()
            else:
                cozulmus_metin += alfabe[yeni_indeks]
        elif karakter.isdigit():
            cozulmus_metin += karakter[::-1]
        else:
            cozulmus_metin += karakter
    return cozulmus_metin

sifreli_metin = input("Lütfen şifreli metni girin: ")
cozulmus_metin = sifre_coz(sifreli_metin)
print("Çözülmüş metin:", cozulmus_metin)

# kullanıcının kendi mesajını şifrelemesi ve şifreledeği mesajı çözülmüş hale döndürmesi

def sifrele_ingilizce(metin):
    alfabe = "abcdefghijklmnopqrstuvwxyz"
    sifreli_metin = ""
    for karakter in metin:
        if karakter.lower() in alfabe:
            indeks = alfabe.find(karakter.lower())
            yeni_indeks = (indeks + 5) % 26  # 26, İngiliz alfabesindeki harf sayısı
            if karakter.isupper():
                sifreli_metin += alfabe[yeni_indeks].upper()
            else:
                sifreli_metin += alfabe[yeni_indeks]
        else:
            sifreli_metin += karakter
    return sifreli_metin

def sifre_coz_ingilizce(sifreli_metin):
    alfabe = "abcdefghijklmnopqrstuvwxyz"
    cozulmus_metin = ""
    for karakter in sifreli_metin:
        if karakter.lower() in alfabe:
            indeks = alfabe.find(karakter.lower())
            yeni_indeks = (indeks - 5) % 26  # 26, İngiliz alfabesindeki harf sayısı
            if karakter.isupper():
                cozulmus_metin += alfabe[yeni_indeks].upper()
            else:
                cozulmus_metin += alfabe[yeni_indeks]
        elif karakter.isdigit():
            cozulmus_metin += karakter[::-1]
        else:
            cozulmus_metin += karakter
    return cozulmus_metin

secim = input("Şifrelemek için '1', çözmek için '2' girin: ")

if secim.lower() == '1':
    metin = input("Şifrelenecek metni girin: ")
    sifreli_metin = sifrele_ingilizce(metin)
    print("Şifreli metin:", sifreli_metin)
elif secim.lower() == '2':
    sifreli_metin = input("Çözülecek şifreli metni girin: ")
    cozulmus_metin = sifre_coz_ingilizce(sifreli_metin)
    print("Çözülmüş metin:", cozulmus_metin)
else:
    print("Geçersiz seçim.")

# "ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl" şifreli mesajı çözülmüş hali "the quick brown fox jumps over the lazy dog"