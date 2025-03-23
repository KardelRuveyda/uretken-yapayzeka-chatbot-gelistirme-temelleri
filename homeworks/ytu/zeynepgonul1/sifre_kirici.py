import string
def decrypt_message(encrypted_text):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[-5:] + alphabet[:-5]  
    decrypt_dict = str.maketrans(shifted_alphabet + shifted_alphabet.upper(), alphabet + alphabet.upper())
    decrypted_text = encrypted_text.translate(decrypt_dict)
    decrypted_text = ''.join(
        str(num)[::-1] if num.isdigit() else num for num in decrypted_text
    )
    return decrypted_text
def encrypt_message(original_text):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[5:] + alphabet[:5]  
    encrypt_dict = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = original_text.translate(encrypt_dict)
    encrypted_text = ''.join(
        str(num)[::-1] if num.isdigit() else num for num in encrypted_text
    )
    return encrypted_text
    
# Sifrelenmis Mesajin Cozumu
encrypted_msg = "ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl"
decrypted_msg = decrypt_message(encrypted_msg)
print("Cozulen Mesaj:", decrypted_msg)

# Mesajlari Sifreleyip Cozebilecek Kod
test_message = "hello 2025!"
encrypted_test = encrypt_message(test_message)
decrypted_test = decrypt_message(encrypted_test)
print("Orijinal Mesaj:", test_message)
print("Sifrelenmis Mesaj:", encrypted_test)
print("Cozulmus Mesaj:", decrypted_test)