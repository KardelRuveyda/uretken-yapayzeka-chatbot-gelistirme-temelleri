import string
import tkinter as tk
from tkinter import messagebox

def shift_character(char, shift):
    if char in string.ascii_lowercase:
        return string.ascii_lowercase[(string.ascii_lowercase.index(char) - shift) % 26]
    elif char in string.ascii_uppercase:
        return string.ascii_uppercase[(string.ascii_uppercase.index(char) - shift) % 26]
    return char

def reverse_number(number):
    return number[::-1]  


def decrypt_message(encrypted_text, shift=5):
    decrypted_text = ""
    temp_number = ""

    for char in encrypted_text:
        if char.isdigit():
            temp_number += char
        else:
            if temp_number:
                decrypted_text += reverse_number(temp_number)
                temp_number = ""
            decrypted_text += shift_character(char, shift)

    if temp_number:
        decrypted_text += reverse_number(temp_number)

    return decrypted_text

#odevdeki sifrelenmis mesaj
print("Sifrelenmiş mesaj:",decrypt_message("ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl"))

def encrypt_message(plain_text, shift=5):
    encrypted_text = ""
    temp_number = ""

    for char in plain_text:
        if char.isdigit():
            temp_number += char
        else:
            if temp_number:
                encrypted_text += reverse_number(temp_number)
                temp_number = ""
            encrypted_text += shift_character(char, -shift)

    if temp_number:
        encrypted_text += reverse_number(temp_number)

    return encrypted_text


def encrypt_action():
    text = entry.get()
    encrypted_text.set(encrypt_message(text))

def decrypt_action():
    text = entry.get()
    decrypted_text.set(decrypt_message(text))


root = tk.Tk()
root.title("Şifreleme ve Çözme Uygulaması")
root.geometry("400x300")

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

encrypted_text = tk.StringVar()
decrypted_text = tk.StringVar()

encrypt_button = tk.Button(root, text="Şifrele", command=encrypt_action)
decrypt_button = tk.Button(root, text="Çöz", command=decrypt_action)

encrypt_button.pack(pady=5)
decrypt_button.pack(pady=5)

encrypted_label = tk.Label(root, textvariable=encrypted_text, fg="blue")
encrypted_label.pack(pady=5)

decrypted_label = tk.Label(root, textvariable=decrypted_text, fg="green")
decrypted_label.pack(pady=5)

root.mainloop()


