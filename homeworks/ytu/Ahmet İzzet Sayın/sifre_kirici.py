def caesar_cipher_custom(text, shift=5):
    result = []
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - shift_base + shift) % 26 + shift_base)) # Karakterlerin şifrelenme biçimi ayarlanır
        elif char.isdigit():
            result.append(char)  # Sayılar şifrelenmez, ters çevrileceği için aynen eklenir
        else:
            result.append(char)  # Boşluklar ve noktalama işaretleri korunur
    return ''.join(result)

def reverse_numbers(text):
    return ''.join(char if not char.isdigit() else '' for char in text) + ''.join(reversed([char for char in text if char.isdigit()]))

def encrypt(text):
    return reverse_numbers(caesar_cipher_custom(text, shift=5))

def decrypt(text):
    return caesar_cipher_custom(reverse_numbers(text), shift=-5)

def main_menu():
    while True:
        print("\n1- Şifreli mesaj çöz")
        print("2- Mesaj şifrele")
        print("3- Çıkış yap")
        choice = input("Seçiminizi yapın (1/2/3): ")

        if choice == "1":
            while True:
                encrypted_text = input("Çözülecek şifreli metni girin: ")
                decrypted_text = decrypt(encrypted_text)
                print("Çözülmüş Metin:", decrypted_text)
                sub_choice = input("Üst menü için 1'e, çıkış yapmak için 2'ye basın: ")
                if sub_choice == "1":
                    break
                elif sub_choice == "2":
                    print("Çıkış yapılıyor...")
                    return

        elif choice == "2":
            while True:
                user_text = input("Şifrelenecek metni girin: ")
                encrypted_user_text = encrypt(user_text)
                print("Şifrelenmiş Metin:", encrypted_user_text)
                sub_choice = input("Üst menü için 1'e, çıkış yapmak için 2'ye basın: ")
                if sub_choice == "1":
                    break
                elif sub_choice == "2":
                    print("Çıkış yapılıyor...")
                    return

        elif choice == "3":
            print("Çıkış yapılıyor...")
            break

        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

# Programı başlat
main_menu()