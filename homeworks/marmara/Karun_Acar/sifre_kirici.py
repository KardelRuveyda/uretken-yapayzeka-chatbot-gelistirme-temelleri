import string

def caesar_cipher(text, shift):
    alphabet = string.ascii_lowercase  # "abcdefghijklmnopqrstuvwxyz"
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]  # Kaydırılmış alfabe
    table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    return text.translate(table)

def encrypt(text):
    return caesar_cipher(text, 5)  # 5 harf ileri

def decrypt(text):
    return caesar_cipher(text, -5)  # 5 harf geri

def reverse_numbers(text):
    return ''.join(char if not char.isdigit() else str(int(char[::-1])) for char in text.split())

def encrypt_message(message):
    words = message.split()
    encrypted_words = [encrypt(word) if word.isalpha() else reverse_numbers(word) for word in words]
    return ' '.join(encrypted_words)

def decrypt_message(message):
    words = message.split()
    decrypted_words = [decrypt(word) if word.isalpha() else reverse_numbers(word) for word in words]
    return ' '.join(decrypted_words)


encrypted_text = "ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl"
decrypted_text = decrypt_message(encrypted_text)
print("Çözülmüş Metin:", decrypted_text)  

user_input = "Merhaba ben 170421049 nolu Karun Acar"

encrypted_user_text = encrypt_message(user_input)
decrypted_user_text = decrypt_message(encrypted_user_text)
print("Kendi mesajım:", decrypted_user_text)
print("Mesajımın şifrelenmiş hali:", encrypted_user_text)



