import string

def sifrele(metin):
    alfabe = string.ascii_lowercase
    sifreli_metin = ""
    
    for karakter in metin:
        if karakter.isalpha():  # Harfse
            kucuk_harf = karakter.lower()
            yeni_index = (alfabe.index(kucuk_harf) + 5) % 26
            yeni_karakter = alfabe[yeni_index]
            if karakter.isupper():
                yeni_karakter = yeni_karakter.upper()
            sifreli_metin += yeni_karakter
        elif karakter.isdigit():  # Rakam ters çevirilecek
            sifreli_metin += karakter[::-1]
        else:
            sifreli_metin += karakter  # Boşluk ve noktalama işaretleri korunur
    
    return sifreli_metin

def coz(metin):
    alfabe = string.ascii_lowercase
    cozulmus_metin = ""
    
    for karakter in metin:
        if karakter.isalpha():  # Harfse
            kucuk_harf = karakter.lower()
            yeni_index = (alfabe.index(kucuk_harf) - 5) % 26
            yeni_karakter = alfabe[yeni_index]
            if karakter.isupper():
                yeni_karakter = yeni_karakter.upper()
            cozulmus_metin += yeni_karakter
        elif karakter.isdigit():  # Rakam ters çevirilecek
            cozulmus_metin += karakter[::-1]
        else:
            cozulmus_metin += karakter  # Boşluk ve noktalama işaretleri korunur
    
    return cozulmus_metin

if __name__ == "__main__":
    print("--- Sifre Kirici Programina Hoş Geldiniz! ---")
    while True:
        secim = input("Sifrelemek için (s), çözmek için (c), çikmak için (q) girin: ")
        if secim == 's':
            metin = input("Sifrelemek istediginiz metni girin: ")
            print("Sifrelenmis metin:", sifrele(metin))
        elif secim == 'c':
            metin = input("Cözmek istediginiz sifreli metni girin: ")
            print("Cozulmus metin:", coz(metin))
        elif secim == 'q':
            print("Çikiş yapiliyor...")
            break
        else:
            print("Gecersiz secm, tekrar deneyin.")