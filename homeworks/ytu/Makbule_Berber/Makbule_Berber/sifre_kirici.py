def sifre_coz(sifreli_metin):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cozulmus_metin = ""

    for char in sifreli_metin:
        if char in alphabet:
            index = alphabet.index(char) - 5
            cozulmus_metin += alphabet[index]
        elif char in alphabet.upper():
            index = alphabet.upper().index(char) - 5
            cozulmus_metin += alphabet.upper()[index]
        elif char.isdigit():
            cozulmus_metin = char + cozulmus_metin
        else:
            cozulmus_metin += char

    return cozulmus_metin

def sifrele(acik_metin):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    sifreli_metin = ""
    sayilar = ""

    for char in acik_metin:
        if char in alphabet:
            index = (alphabet.index(char) + 5) % 26
            sifreli_metin += alphabet[index]
        elif char in alphabet.upper():
            index = (alphabet.upper().index(char) + 5) % 26
            sifreli_metin += alphabet.upper()[index]
        elif char.isdigit():
            sayilar = char + sayilar
        else:
            sifreli_metin += sayilar + char
            sayilar = ""
    sifreli_metin += sayilar

    return sifreli_metin

# Şifrelenmiş mesajı çöz
encrypted_text = "ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl"
cozulmus_metin = sifre_coz(encrypted_text)
print("Çözülmüş Mesaj:", cozulmus_metin)

# Kullanıcıdan giriş alarak şifreleme ve çözme işlemi
test_message = input("Şifrelemek istediğiniz metni girin: ")
sifreli = sifrele(test_message)
print("Şifrelenmiş Mesaj:", sifreli)

cozulmus = sifre_coz(sifreli)
print("Çözülmüş Mesaj:", cozulmus)

# Kullanıcıdan şifrelenmiş mesaj alıp çözme
sifreli_giris = input("Çözmek istediğiniz şifreli mesajı girin: ")
cozulmus_giris = sifre_coz(sifreli_giris)
print("Çözülmüş Mesaj:", cozulmus_giris)
