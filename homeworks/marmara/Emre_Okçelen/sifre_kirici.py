import string
import re

#Emre Okçelen 170421929 Marmara

def shift_letter(letter, shift):
    alphabet = string.ascii_lowercase
    alphabet_upper = string.ascii_uppercase

    if letter in alphabet:
        return alphabet[(alphabet.index(letter) + shift) % 26]
    elif letter in alphabet_upper:
        return alphabet_upper[(alphabet_upper.index(letter) + shift) % 26]
    return letter

def reverse_numbers_in_text(text):
    return re.sub(r'\d+', lambda num: num.group(0)[::-1], text)

def encrypt(text, shift=5):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            encrypted_text += shift_letter(char, shift)
        else:
            encrypted_text += char

    return reverse_numbers_in_text(encrypted_text)

def decrypt(text, shift=-5):
    text = reverse_numbers_in_text(text)
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            decrypted_text += shift_letter(char, shift)
        else:
            decrypted_text += char

    return decrypted_text

encrypted_message = "ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl"
decrypted_message = decrypt(encrypted_message)
print(f"Decrypted Message: {decrypted_message}")

user_input = input("Enter a message to encrypt (Example Sentce: Emre Okcelen 170421929): ") #User Input
encrypted_user_message = encrypt(user_input)
print(f"Encrypted Message: {encrypted_user_message}")

decrypted_user_message = decrypt(encrypted_user_message)
print(f"Decrypted Message: {decrypted_user_message}")
