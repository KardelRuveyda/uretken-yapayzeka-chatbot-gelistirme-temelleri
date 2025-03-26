# homeworks/
#     ├── marmara/
#     │   ├── Tugdil_Kalkan/
#     │   │   ├── sifre_kirici.py

import string

def decrypt_message(encrypted_text):
    alphabet = string.ascii_lowercase
    shift = 5
    decrypted_text = ""
    
    for char in encrypted_text:
        if char in alphabet:
            new_index = (alphabet.index(char) - shift) % 26
            decrypted_text += alphabet[new_index]
        else:
            decrypted_text += char
    
    return decrypted_text

def encrypt_message(plain_text):
    alphabet = string.ascii_lowercase
    shift = 5
    encrypted_text = ""
    
    for char in plain_text:
        if char in alphabet:
            new_index = (alphabet.index(char) + shift) % 26
            encrypted_text += alphabet[new_index]
        else:
            encrypted_text += char
    
    return encrypted_text

# Şifrelenmiş mesajı çözme
encrypted_message = "ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl"
decrypted_message = decrypt_message(encrypted_message)
print("Çözülen Mesaj:", decrypted_message)

# Kullanıcıdan giriş alarak mesaj şifreleme ve çözme
def main():
    user_input = input("Şifrelemek istediğiniz mesajı girin: ")
    encrypted = encrypt_message(user_input.lower())
    print("Şifrelenmiş Mesaj:", encrypted)
    
    decrypted = decrypt_message(encrypted)
    print("Çözülen Mesaj:", decrypted)

if __name__ == "__main__":
    main()
    