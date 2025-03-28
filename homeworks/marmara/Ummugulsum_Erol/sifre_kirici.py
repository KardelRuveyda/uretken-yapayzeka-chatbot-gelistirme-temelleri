import re

def decrypt_message(encrypted_message):
    decrypted_chars = []
    numbers = re.findall(r'\d+', encrypted_message) 
    reversed_numbers = [num[::-1] for num in numbers] 
    number_index = 0
    
    for char in encrypted_message:
        if char.isalpha():
            base = 'a' if char.islower() else 'A'
            decrypted_char = chr((ord(char) - ord(base) - 5) % 26 + ord(base))
            decrypted_chars.append(decrypted_char)
        elif char.isdigit():
            if number_index < len(reversed_numbers):
                decrypted_chars.append(reversed_numbers[number_index])
                number_index += 1
        else:
            decrypted_chars.append(char)
    
    return ''.join(decrypted_chars)

def encrypt_message(original_message):
    encrypted_chars = []
    numbers = re.findall(r'\d+', original_message)
    reversed_numbers = [num[::-1] for num in numbers]
    number_index = 0
    
    for char in original_message:
        if char.isalpha():
            base = 'a' if char.islower() else 'A'
            encrypted_char = chr((ord(char) - ord(base) + 5) % 26 + ord(base))
            encrypted_chars.append(encrypted_char)
        elif char.isdigit():
            if number_index < len(reversed_numbers):
                encrypted_chars.append(reversed_numbers[number_index])
                number_index += 1
        else:
            encrypted_chars.append(char)
    
    return ''.join(encrypted_chars)

encrypted_message = "ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl"
decrypted_message = decrypt_message(encrypted_message)
print("Şifrelenmiş Mesaj:", encrypted_message)
print("Çözülmüş Mesaj:", decrypted_message)

def main():
    while True:
        print("\n--- Şifre Çözücü/Şifreleyici ---")
        print("1. Mesaj Şifrele")
        print("2. Mesaj Çöz")
        print("3. Çıkış")
        
        choice = input("Seçiminizi yapın (1/2/3): ")
        
        if choice == '1':
            message = input("Şifrelemek istediğiniz mesajı girin: ")
            encrypted_message = encrypt_message(message)
            print("Şifrelenmiş mesaj:", encrypted_message)
        
        elif choice == '2':
            message = input("Çözmek istediğiniz şifreli mesajı girin: ")
            decrypted_message = decrypt_message(message)
            print("Çözülmüş mesaj:", decrypted_message)
        
        elif choice == '3':
            print("Programdan çıkılıyor...")
            break
        
        else:
            print("Geçersiz seçim. Lütfen 1, 2 veya 3 seçeneklerinden birini seçin.")

if __name__ == "__main__":
    main()
 