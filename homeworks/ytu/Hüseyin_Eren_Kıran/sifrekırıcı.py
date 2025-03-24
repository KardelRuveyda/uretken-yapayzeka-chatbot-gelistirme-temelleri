def harf_sifre_coz(karakter):
    """Bir harfi alfabede 5 pozisyon geriye kaydırarak şifresini çözer."""
    if not karakter.isalpha():
        return karakter
    
    # Temel değeri belirle (ASCII kodu 'a' veya 'A' için)
    temel = ord('a') if karakter.islower() else ord('A')
    
    # 5 pozisyon geriye kaydır, alfabenin başına sarma ile
    kaydirma = (ord(karakter) - temel - 5) % 26 + temel
    return chr(kaydirma)

def harf_sifrele(karakter):
    """Bir harfi alfabede 5 pozisyon ileriye kaydırarak şifreler."""
    if not karakter.isalpha():
        return karakter
    
    # Temel değeri belirle (ASCII kodu 'a' veya 'A' için)
    temel = ord('a') if karakter.islower() else ord('A')
    
    # 5 pozisyon ileriye kaydır, alfabenin başına sarma ile
    kaydirma = (ord(karakter) - temel + 5) % 26 + temel
    return chr(kaydirma)

def sayilari_isle(metin, tersine=True):
    """Metindeki sayıları bulup ters çevirir."""
    sonuc = ""
    i = 0
    
    while i < len(metin):
        if metin[i].isdigit():
            # Tam sayıyı bul
            baslangic = i
            while i < len(metin) and metin[i].isdigit():
                i += 1
            
            # Sayıyı çıkar ve tersine çevir
            sayi = metin[baslangic:i]
            if tersine:
                ters_sayi = sayi[::-1]
                sonuc += ters_sayi
            else:
                sonuc += sayi
        else:
            sonuc += metin[i]
            i += 1
            
    return sonuc

def sifre_coz(sifreli_metin):
    """Verilen metni şifreleme algoritmasının tersini kullanarak çözer."""
    # Önce harfleri işle (5 pozisyon geriye kaydır)
    cozulmus_metin = ''.join(harf_sifre_coz(karakter) for karakter in sifreli_metin)
    
    # Sonra metindeki sayıları ters çevir
    cozulmus_metin = sayilari_isle(cozulmus_metin, tersine=True)
    
    return cozulmus_metin

def sifrele(duz_metin):
    """Verilen metni şifreleme algoritmasını kullanarak şifreler."""
    # Önce metindeki sayıları ters çevir
    islenmis_metin = sayilari_isle(duz_metin, tersine=True)
    
    # Sonra harfleri işle (5 pozisyon ileriye kaydır)
    sifreli_metin = ''.join(harf_sifrele(karakter) for karakter in islenmis_metin)
    
    return sifreli_metin

def main():
    print("🔐 Şifreleme/Şifre Çözme Programı 🔓")
    print("------------------------------------")
    
    # Verilen şifreli mesajı çöz
    sifreli_mesaj = "ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl"
    cozulmus_mesaj = sifre_coz(sifreli_mesaj)
    
    print(f"\n🔑 Şifreli mesaj: {sifreli_mesaj}")
    print(f"🔓 Çözülmüş mesaj: {cozulmus_mesaj}")
    
    # Kullanıcının kendi mesajları için etkileşimli mod
    print("\n✨ Bonus Özellik: Kendi mesajlarınızı deneyin ✨")
    while True:
        print("\nBir seçenek belirleyin:")
        print("1. Bir mesajı şifrele")
        print("2. Bir mesajın şifresini çöz")
        print("3. Çıkış")
        
        secim = input("Seçiminizi girin (1/2/3): ")
        
        if secim == '1':
            mesaj = input("\nŞifrelenecek mesajı girin: ")
            sifreli = sifrele(mesaj)
            print(f"🔒 Şifrelenmiş: {sifreli}")
        elif secim == '2':
            mesaj = input("\nŞifresi çözülecek mesajı girin: ")
            cozulmus = sifre_coz(mesaj)
            print(f"🔓 Şifresi çözülmüş: {cozulmus}")
        elif secim == '3':
            print("\nŞifreleme/şifre çözme programını kullandığınız için teşekkürler!")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
