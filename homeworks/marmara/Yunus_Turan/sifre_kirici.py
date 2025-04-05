# Yunus Alp Turan - 171421001
import os
import time
from colorama import Fore, Style, init

init(autoreset=True)  # Colorama otomatik sıfırlama


class Kodlayici:
    def __init__(self, kaydirma=5):
        self.kaydirma = kaydirma
        self.kucuk = 'abcdefghijklmnopqrstuvwxyz'
        self.buyuk = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def kaydir(self, karakter, miktar):
        """Verilen karakteri, belirtilen miktarda kaydırır."""
        if karakter in self.kucuk:
            yeni_index = (self.kucuk.index(karakter) + miktar) % 26
            return self.kucuk[yeni_index]
        elif karakter in self.buyuk:
            yeni_index = (self.buyuk.index(karakter) + miktar) % 26
            return self.buyuk[yeni_index]
        else:
            return karakter

    def sayilari_tersle(self, metin):
        """Metindeki rakam dizilerini ters çevirir."""
        sonuc = []
        rakamlar = ""
        for ch in metin:
            if ch.isdigit():
                rakamlar += ch
            else:
                if rakamlar:
                    sonuc.append(rakamlar[::-1])
                    rakamlar = ""
                sonuc.append(ch)
        if rakamlar:
            sonuc.append(rakamlar[::-1])
        return "".join(sonuc)

    def sifrele(self, metin):
        """Metni şifreler: harfleri kaydırır, sayıları ters çevirir."""
        sifreli = "".join(self.kaydir(ch, self.kaydirma) for ch in metin)
        return self.sayilari_tersle(sifreli)

    def coz(self, metin):
        """Şifrelenmiş metnin orijinal halini geri getirir."""
        oncelikle_ters = self.sayilari_tersle(metin)
        cozulmus = "".join(self.kaydir(ch, -self.kaydirma) for ch in oncelikle_ters)
        return cozulmus


def ekran_temizle():
    os.system('cls' if os.name == 'nt' else 'clear')


def menu_goster():
    ekran_temizle()
    print(Fore.CYAN + "=" * 40)
    print(Fore.YELLOW + "🔐 Şifreleme ve Çözüm Aracı".center(40))
    print(Fore.CYAN + "=" * 40)
    print(Fore.GREEN + "1 - Örnek Şifreli Mesajı Göster ve Çöz")
    print(Fore.BLUE + "2 - Kullanıcıdan Şifreli Mesaj Al ve Çöz")
    print(Fore.MAGENTA + "3 - Girdiğiniz Metni Şifrele")
    print(Fore.RED + "0 - Çıkış")
    print(Fore.CYAN + "=" * 40)


def main():
    arac = Kodlayici()
    hatali = 0

    while True:
        menu_goster()
        secim = input(Fore.YELLOW + "\nLütfen seçiminizi yapın: ")

        if secim in ["1", "2", "3", "0"]:
            hatali = 0  # Doğru giriş yapıldığında hatalar sıfırlansın

        if secim == "1":
            print(Fore.CYAN + "\nÖrnek mesaj hazırlanıyor...")
            ornek_sifre = "ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl"
            ornek_cozum = arac.coz(ornek_sifre)
            print(Fore.GREEN + f"Şifreli Mesaj: {ornek_sifre}")
            print(Fore.BLUE + f"Çözülmüş Mesaj: {ornek_cozum}")
            input(Fore.YELLOW + "\nDevam etmek için Enter'e basın...")

        elif secim == "2":
            kullanici_sifre = input(Fore.YELLOW + "\nŞifreli mesajınızı yazın: ")
            sonuc = arac.coz(kullanici_sifre)
            print(Fore.BLUE + f"Çözüm Sonucu: {sonuc}")
            input(Fore.YELLOW + "\nDevam etmek için Enter'e basın...")

        elif secim == "3":
            kullanici_metin = input(Fore.YELLOW + "\nŞifrelemek istediğiniz metni girin: ")
            sifrelenmis = arac.sifrele(kullanici_metin)
            print(Fore.GREEN + f"Orijinal Metin: {kullanici_metin}")
            print(Fore.MAGENTA + f"Şifrelenmiş Metin: {sifrelenmis}")
            input(Fore.YELLOW + "\nDevam etmek için Enter'e basın...")

        elif secim == "0":
            print(Fore.RED + "\nProgram kapatılıyor...")
            break

        else:
            hatali += 1
            print(Fore.RED + f"\nGeçersiz seçim! Kalan deneme hakkı: {3 - hatali}")
            time.sleep(1)
            if hatali >= 3:
                print(Fore.RED + "\nÇok fazla hatalı giriş. Program sonlandırılıyor...")
                break


if __name__ == "__main__":
    main()
