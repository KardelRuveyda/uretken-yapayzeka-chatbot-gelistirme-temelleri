def caesar_cipher_custom(text, shift=5):
    result = []
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - shift_base + shift) % 26 + shift_base))
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

#github için deneme terminalden pushlamaya çalışıcam

# Örnek kullanım
encrypted_text = "ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl"
decrypted_text = decrypt(encrypted_text)

print("Çözülen Metin:", decrypted_text)

# Kullanıcının kendi mesajını şifreleyip çözmesi için giriş alalım:
user_text = input("Şifrelenecek metni girin: ")
encrypted_user_text = encrypt(user_text)
decrypted_user_text = decrypt(encrypted_user_text)

print("Şifrelenmiş Metin:", encrypted_user_text)
print("Çözülmüş Metin:", decrypted_user_text)

#deneme