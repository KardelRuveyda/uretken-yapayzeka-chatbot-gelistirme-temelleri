def encrypt_text(original_text):
    encrypted_text = ""
    index = 0

    while index < len(original_text):
        char = original_text[index]

        if 'a' <= char <= 'z':
            new_char = chr(ord(char) + 5)
            if new_char > 'z':
                new_char = chr(ord(new_char) - 26)
            encrypted_text += new_char

        elif 'A' <= char <= 'Z':
            new_char = chr(ord(char) + 5)
            if new_char > 'Z':
                new_char = chr(ord(new_char) - 26)
            encrypted_text += new_char

        else:
            encrypted_text += char

        index += 1

    return encrypted_text

def reverse_numbers(text):
    encrypted_text = ""
    index = 0

    while index < len(text):
        if '0' <= text[index] <= '9':
            num_start = index
            while index < len(text) and '0' <= text[index] <= '9':
                index += 1
            encrypted_text += text[num_start:index][::-1]
        else:
            encrypted_text += text[index]
            index += 1

    return encrypted_text

def full_encryption(user_text):
    step1 = reverse_numbers(user_text)
    return encrypt_text(step1)

def decrypt_text(encrypted_text):
    decrypted_text = ""
    index = 0
    while index < len(encrypted_text):
        char = encrypted_text[index]

        if 'a' <= char <= 'z':
            new_char = chr(ord(char) - 5)
            if new_char < 'a':
                new_char = chr(ord(new_char) + 26)
            decrypted_text += new_char

        elif 'A' <= char <= 'Z':
            new_char = chr(ord(char) - 5)
            if new_char < 'A':
                new_char = chr(ord(new_char) + 26)
            decrypted_text += new_char

        else:
            decrypted_text += char

        index += 1

    return decrypted_text

def full_decryption(encrypted_message):
    """Tam çözümleme işlemi: önce harfleri düzelt, sonra sayıları ters çevir."""
    step1 = decrypt_text(encrypted_message)
    return reverse_numbers(step1)


user_input = input("Şifrelemek istediğiniz mesajı girin: ")
encrypted_output = full_encryption(user_input)
print("Şifrelenmiş Mesaj:", encrypted_output)

decrypted_output = full_decryption(encrypted_output)
print("Çözülen Mesaj:", decrypted_output)
