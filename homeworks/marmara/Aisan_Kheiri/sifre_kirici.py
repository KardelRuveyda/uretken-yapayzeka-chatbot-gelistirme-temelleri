import string

# Sayıları ters çeviren fonksiyon
def reverse_number(num_str):
    return num_str[::-1]

# Şifrelenmiş mesajı çözen fonksiyon
def decrypt_message(encrypted_text):
    alphabet = string.ascii_lowercase
    shift = 5
    decrypted_text = ""
    temp_number = ""
    
    for char in encrypted_text:
        if char.isdigit():
            temp_number += char  # Sayıları geçici olarak biriktir
        else:
            if temp_number:
                decrypted_text += reverse_number(temp_number)  # Biriken sayıyı ters çevir ve ekle
                temp_number = ""
            
            if char.isalpha():
                is_upper = char.isupper()
                char = char.lower()
                new_index = (alphabet.index(char) - shift) % 26
                new_char = alphabet[new_index]
                decrypted_text += new_char.upper() if is_upper else new_char
            else:
                decrypted_text += char
    
    if temp_number:
        decrypted_text += reverse_number(temp_number)  # Metnin sonunda kalan sayıyı ters çevir
    
    return decrypted_text

# Mesajı şifreleyen fonksiyon
def encrypt_message(original_text):
    alphabet = string.ascii_lowercase
    shift = 5
    encrypted_text = ""
    temp_number = ""
    
    for char in original_text:
        if char.isdigit():
            temp_number += char  # Sayıları biriktir
        else:
            if temp_number:
                encrypted_text += reverse_number(temp_number)  # Biriken sayıyı ters çevir ve ekle
                temp_number = ""
            
            if char.isalpha():
                is_upper = char.isupper()
                char = char.lower()
                new_index = (alphabet.index(char) + shift) % 26
                new_char = alphabet[new_index]
                encrypted_text += new_char.upper() if is_upper else new_char
            else:
                encrypted_text += char
    
    if temp_number:
        encrypted_text += reverse_number(temp_number)  # Metnin sonunda kalan sayıyı ters çevir
    
    return encrypted_text

# Homework şifreleme ve çözme işlemi
original_text = "ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl"
encrypted_text = encrypt_message(original_text)
decrypted_text = decrypt_message(encrypted_text)

print("Original Text:", original_text)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)

# Kendi Bilgilerim şifreleme ve çözme işlemi
own_text = "Aisan Kheiri 170420995"
encrypted_own_text = encrypt_message(own_text)
decrypted_own_text = decrypt_message(encrypted_own_text)

print("Own Text:", own_text)
print("Encrypted Own Text:", encrypted_own_text)
print("Decrypted Own Text:", decrypted_own_text)

# Kullanıcıdan giriş alarak şifreleme ve çözme işlemi
user_input = input("Şifrelemek istediğiniz metni girin: ")
encrypted_user_input = encrypt_message(user_input)
decrypted_user_input = decrypt_message(encrypted_user_input)

print("Encrypted User Input:", encrypted_user_input)
print("Decrypted User Input:", decrypted_user_input)


