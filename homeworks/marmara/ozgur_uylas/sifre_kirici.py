import logging
from abc import ABC, abstractmethod


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="sifre_kirici.log",
    filemode="a"
)


class Cipher(ABC):
    @abstractmethod
    def encrypt(self, text):
        pass

    @abstractmethod
    def decrypt(self, text):
        pass


class LetterCipher(Cipher):
    def __init__(self, shift=5):
        self.__shift = shift

    def encrypt(self, text):
        result = ""
        for char in text:
            if char.isalpha():
                if char.islower():
                    result += chr((ord(char) - ord('a') + self.__shift) % 26 + ord('a'))
                else:
                    result += chr((ord(char) - ord('A') + self.__shift) % 26 + ord('A'))
            else:
                result += char
        logging.info("Harf şifrelendi: %s → %s", text, result)
        return result

    def decrypt(self, text):
        result = ""
        for char in text:
            if char.isalpha():
                if char.islower():
                    result += chr((ord(char) - ord('a') - self.__shift) % 26 + ord('a'))
                else:
                    result += chr((ord(char) - ord('A') - self.__shift) % 26 + ord('A'))
            else:
                result += char
        logging.info("Harf çözüldü: %s → %s", text, result)
        return result


class NumberCipher(Cipher):
    def encrypt(self, text):
        reversed_text = text[::-1]
        logging.info("Sayı şifrelendi: %s → %s", text, reversed_text)
        return reversed_text

    def decrypt(self, text):
        reversed_text = text[::-1]
        logging.info("Sayı çözüldü: %s → %s", text, reversed_text)
        return reversed_text


class SifreKirici:
    def __init__(self, letter_cipher: Cipher, number_cipher: Cipher):
        self.letter_cipher = letter_cipher
        self.number_cipher = number_cipher
        logging.info("SifreKirici başlatıldı")

    def cozumle(self, sifreli_metin):
        kelimeler = sifreli_metin.split()
        sonuc = []
        for kelime in kelimeler:
            if kelime.isdigit():
                sonuc.append(self.number_cipher.decrypt(kelime))
            else:
                sonuc.append(self.letter_cipher.decrypt(kelime))
        return " ".join(sonuc)

    def sifrele(self, metin):
        kelimeler = metin.split()
        sonuc = []
        for kelime in kelimeler:
            if kelime.isdigit():
                sonuc.append(self.number_cipher.encrypt(kelime))
            else:
                sonuc.append(self.letter_cipher.encrypt(kelime))
        return " ".join(sonuc)

    def calistir(self):
        logging.info("Program çalıştırıldı")
        print(" Şifreli Mesaj: ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl")
        orijinal = self.cozumle("ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl")
        print("Çözülmüş Mesaj:", orijinal)

        while True:
            print("\n--- Şifre Kırıcı Menü ---")
            print("1. Mesaj şifrele")
            print("2. Mesaj çöz")
            print("3. Çıkış")
            secim = input("Seçiminiz: ")
            if secim == "1":
                mesaj = input("Şifrelenecek mesaj: ")
                sonuc = self.sifrele(mesaj)
                print("Şifreli:", sonuc)
            elif secim == "2":
                mesaj = input("Çözülecek mesaj: ")
                sonuc = self.cozumle(mesaj)
                print("Çözüm:", sonuc)
            elif secim == "3":
                logging.info("Kullanıcı çıkış yaptı.")
                print("Güle güle!")
                break
            else:
                print("Geçersiz seçim.")

if __name__ == "__main__":
    harf_sifreleyici = LetterCipher()
    sayi_sifreleyici = NumberCipher()
    uygulama = SifreKirici(harf_sifreleyici, sayi_sifreleyici)
    uygulama.calistir()
