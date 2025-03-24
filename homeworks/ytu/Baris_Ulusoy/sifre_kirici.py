# Baris Ulusoy
def harf_coz(harf):
    if harf.isalpha():
        alfabe = 'abcdefghijklmnopqrstuvwxyz'
        index = alfabe.find(harf.lower())
        yeni_index = (index - 5) % 26
        yeni_harf = alfabe[yeni_index]
        return yeni_harf.upper() if harf.isupper() else yeni_harf
    else:
        return harf

def harf_sifrele(harf):
    if harf.isalpha():
        alfabe = 'abcdefghijklmnopqrstuvwxyz'
        index = alfabe.find(harf.lower())
        yeni_index = (index + 5) % 26
        yeni_harf = alfabe[yeni_index]
        return yeni_harf.upper() if harf.isupper() else yeni_harf
    else:
        return harf

def metni_coz(metin):
    sonuc = ""
    for karakter in metin:
        if karakter.isdigit():
            sonuc += karakter  
        else:
            sonuc += harf_coz(karakter)
    return sonuc

def metni_sifrele(metin):
    sonuc = ""
    for karakter in metin:
        if karakter.isdigit():
            sonuc += karakter  
        else:
            sonuc += harf_sifrele(karakter)
    return sonuc

# Ana program
secim = input("Şifrelemek için (s), çözmek için (c) yazın: ").lower()
girdi = input("Metni girin: ")

if secim == "s":
    print("Şifrelenmiş:", metni_sifrele(girdi))
elif secim == "c":
    print("Çözülmüş:", metni_coz(girdi))
else:
    print("Geçersiz seçim.")
