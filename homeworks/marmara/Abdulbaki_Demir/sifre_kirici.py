def string_decryptor(encrypted_string_data, decrypt_value):
    # Decrypts a given string using a Caesar cipher-like method.
    # Each letter is shifted back by `decrypt_value` positions.
    content = ""  # Variable to store the decrypted string
    for i in encrypted_string_data.lower():
        alp_index = 0
        if i.isalpha():  # Check if character is an alphabet letter
            number_of_char = ord(i)
            if number_of_char < 97 + decrypt_value:  # Handle wrap-around cases
                alp_index = 26 - (decrypt_value - number_of_char)
            else:
                alp_index = number_of_char - decrypt_value
            content += chr(alp_index)
        else:
            content += i  # Preserve non-alphabet characters
    return content

def decryptor(encrypted_data, decrypt_value=5):
    # Decrypts an entire string, word by word.
    # Numeric words are reversed instead of being decrypted.
    data = []
    for i in encrypted_data.split():
        if i.isnumeric():  # Check if the word is numeric
            data.append(i[::-1])  # Reverse numeric values
        else:
            data.append(string_decryptor(i, decrypt_value))
    return " ".join(data)

def string_encryptor(decrypted_data, encrypt_value):
    # Encrypts a given string using a Caesar cipher-like method.
    # Each letter is shifted forward by `encrypt_value` positions.
    content = ""  # Variable to store the encrypted string
    for i in decrypted_data.lower():
        alp_index = 0
        if i.isalpha():  # Check if character is an alphabet letter
            number_of_char = ord(i)
            if number_of_char > 122 - encrypt_value:  # Handle wrap-around cases
                alp_index = -26 + (number_of_char + encrypt_value)
            else:
                alp_index = number_of_char + encrypt_value
            content += chr(alp_index)
        else:
            content += i  # Preserve non-alphabet characters
    return content

def encryptor(decrypted_data, encrypt_value=5):
    # Encrypts an entire string, word by word.
    # Numeric words are reversed instead of being encrypted.
    data = []
    for i in decrypted_data.split():
        if i.isnumeric():  # Check if the word is numeric
            data.append(i[::-1])  # Reverse numeric values
        else:
            data.append(string_encryptor(i, encrypt_value))
    return " ".join(data)

# Main program
print("Welcome to the Encryptor/Decryptor\n\n\n")

print("ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl")
print(decryptor("ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl", 5),"\n\n\n")

# encrypt_value: The shift value used for encryption and decryption.
# It determines how many positions each letter is shifted in the Caesar cipher.

print("Set the shift value for encryption/decryption")
encrypt_value = int(input("Enter the value to encrypt/decrypt: "))

while True:
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Set the value to encrypt/decrypt")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        # Encrypt user input
        data = input("Enter the data to encrypt: ")
        print("Encrypt Data: ", encryptor(data, encrypt_value), end="\n\n")
    elif choice == 2:
        # Decrypt user input
        data = input("Enter the data to decrypt: ")
        print("Decrypt Data: ", decryptor(data, encrypt_value), end="\n\n")
    elif choice == 3:
        # Update the shift value for encryption/decryption
        encrypt_value = int(input("Enter the value to encrypt/decrypt: "))  
    elif choice == 4:
        # Exit the program
        break
    else:
        print("Invalid choice")
        continue