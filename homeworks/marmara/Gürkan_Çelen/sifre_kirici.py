#Gürkan Çelen-171421004
import os
import time
from colorama import Fore, Style, init

init(autoreset=True)  # Colorama otomatik sıfırlama

class Cipher:
    def __init__(self, shift=5):
        self.shift = shift
        self.alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
        self.alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def _shift_char(self, char, shift_amount):
        """Harfleri belirli bir kaydırma miktarına göre değiştirir."""
        if char in self.alphabet_lower:
            new_index = (self.alphabet_lower.index(char) + shift_amount) % 26
            return self.alphabet_lower[new_index]
        elif char in self.alphabet_upper:
            new_index = (self.alphabet_upper.index(char) + shift_amount) % 26
            return self.alphabet_upper[new_index]
        return char  # Harf değilse değiştirme
    
    def _reverse_numbers(self, text):
        """Metindeki sayıları ters çevirir."""
        reversed_numbers = []
        temp_number = ""
        
        for char in text:
            if char.isdigit():
                temp_number += char
            else:
                if temp_number:
                    reversed_numbers.append(temp_number[::-1])  # Sayıyı ters çevir
                    temp_number = ""
                reversed_numbers.append(char)  # Sayı değilse olduğu gibi ekle
        
        if temp_number:
            reversed_numbers.append(temp_number[::-1])  # Son rakamları ekle
        
        return "".join(reversed_numbers)

    def encrypt(self, text):
        """Verilen metni şifreler."""
        encrypted_text = "".join(self._shift_char(char, self.shift) for char in text)
        return self._reverse_numbers(encrypted_text)

    def decrypt(self, text):
        """Verilen şifrelenmiş metni çözer."""
        reversed_text = self._reverse_numbers(text)  # Önce sayıları geri çevir
        decrypted_text = "".join(self._shift_char(char, -self.shift) for char in reversed_text)
        return decrypted_text


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu():
    clear_screen()
    print(Fore.CYAN + "=" * 50)
    print(Fore.YELLOW + "🚀 ŞİFRELEME PROGRAMI".center(50))
    print(Fore.CYAN + "=" * 50)
    print(Fore.GREEN + "1 - 📜 Örnek Şifreli Mesajı Göster ve Çöz")
    print(Fore.BLUE + "2 - 🎭 Kullanıcının Şifreli Mesajını Çöz")
    print(Fore.MAGENTA + "3 - 🔄 Kullanıcının Mesajını Şifrele")
    print(Fore.RED + "0 - ❌ Çıkış")
    print(Fore.CYAN + "=" * 50)

def main():
    cipher = Cipher()
    incorrect_attempts = 0
    
    while True:
        print_menu()
        
        choice = input(Fore.YELLOW + "\nLütfen bir seçenek girin: ")
        
        if choice in ["1", "2", "3", "0"]:
            incorrect_attempts = 0  # Doğru giriş yapılınca hatalar sıfırlanır
        
        if choice == "1":
            print(Fore.CYAN + "\n📜 Örnek Şifreli Mesaj Gösteriliyor...")
            encrypted_message = "ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl"
            decrypted_message = cipher.decrypt(encrypted_message)
            print(Fore.GREEN + f"🔒 Şifreli Mesaj: {encrypted_message}")
            print(Fore.BLUE + f"🔄 Çözülen Mesaj: {decrypted_message}")
            input(Fore.YELLOW + "\nDevam etmek için Enter'a basın...")

        elif choice == "2":
            user_encrypted = input(Fore.YELLOW + "\n🎭 Şifreli mesajınızı girin: ")
            decrypted_user_message = cipher.decrypt(user_encrypted)
            print(Fore.BLUE + f"🔄 Çözülen Mesaj: {decrypted_user_message}")
            input(Fore.YELLOW + "\nDevam etmek için Enter'a basın...")

        elif choice == "3":
            user_input = input(Fore.YELLOW + "\n📜 Şifrelemek istediğiniz metni girin: ")
            encrypted = cipher.encrypt(user_input)
            print(Fore.GREEN + f"✅ Orijinal Metin: {user_input}")
            print(Fore.MAGENTA + f"🎭 Şifrelenmiş Metin: {encrypted}")
            input(Fore.YELLOW + "\nDevam etmek için Enter'a basın...")

        elif choice == "0":
            print(Fore.RED + "\n❌ Programdan çıkılıyor...")
            break

        else:
            incorrect_attempts += 1
            print(Fore.RED + f"\n⚠️ Hatalı giriş! Kalan deneme hakkı: {3 - incorrect_attempts}")
            time.sleep(0.5)

            if incorrect_attempts >= 3:
                print(Fore.RED + "\n❌ Çok fazla hatalı giriş yapıldı. Program sonlandırılıyor...")
                break

if __name__ == "__main__":
    main()
