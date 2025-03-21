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

def reverse_numbers(text):
    decrypted_text = ""
    index = 0

    while index < len(text):
        if '0' <= text[index] <= '9':
            num_start = index
            while index < len(text) and '0' <= text[index] <= '9':
                index += 1
            decrypted_text += text[num_start:index][::-1]
        else:
            decrypted_text += text[index]
            index += 1

    return decrypted_text

def full_decryption(encrypted_message):
    step1 = decrypt_text(encrypted_message)
    return reverse_numbers(step1)

encrypted_text = "ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl"

decrypted_result = full_decryption(encrypted_text)
print("Orijinal Mesaj:", decrypted_result)
