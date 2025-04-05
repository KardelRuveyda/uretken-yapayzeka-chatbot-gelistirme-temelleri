class CryptHelper:
    def __init__(self):
        self.sample = "ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl"
        self.alphabet_size = 26
        self.shift_size = 5

    def encrypt(self, message):
        encrypted_message = ""
        num_buffer = []

        for char in message:
            if char.isalpha():
                if num_buffer:
                    encrypted_message += ''.join(num_buffer[::-1])
                    num_buffer = []
                if char.islower():
                    encrypted_char = chr((ord(char) - ord('a') + self.shift_size) % self.alphabet_size + ord('a'))
                elif char.isupper():
                    encrypted_char = chr((ord(char) - ord('A') + self.shift_size) % self.alphabet_size + ord('A'))
                encrypted_message += encrypted_char
            elif char.isdigit():
                num_buffer.append(char)
            else:
                if num_buffer:
                    encrypted_message += ''.join(num_buffer[::-1])
                    num_buffer = []
                encrypted_message += char

        if num_buffer:
            encrypted_message += ''.join(num_buffer[::-1])

        return encrypted_message

    def decrypt(self, message):
        decrypted_message = ""
        num_buffer = []

        for char in message:
            if char.isalpha():
                if num_buffer:
                    decrypted_message += ''.join(num_buffer[::-1])
                    num_buffer = []
                if char.islower():
                    decrypted_char = chr((ord(char) - ord('a') - self.shift_size) % self.alphabet_size + ord('a'))
                elif char.isupper():
                    decrypted_char = chr((ord(char) - ord('A') - self.shift_size) % self.alphabet_size + ord('A'))
                decrypted_message += decrypted_char
            elif char.isdigit():
                num_buffer.append(char)
            else:
                if num_buffer:
                    decrypted_message += ''.join(num_buffer[::-1])
                    num_buffer = [] 
                decrypted_message += char

        if num_buffer:
            decrypted_message += ''.join(num_buffer[::-1])

        return decrypted_message

cryptHelper = CryptHelper()

print("\n")
print(f"{'Şifre Kırıcı programına hoş geldiniz!':^50}")

while True:
    print("*" * 50)
    print(f"* {'1 - 🧩 Örnek mesajı çöz':^45} *")
    print(f"* {'2 - 🔐 Kendi mesajını şifrele':^45} *") 
    print(f"* {'3 - 🗝️ Şifrelenmiş mesajı çöz':^47} *")
    print(f"* {'4 - 🚪 Çıkış yap':^45} *")
    print("*" * 50)
    
    choice = input("\nSeçiminizi girin: ")

    if choice == '1':
        decrypted_example = cryptHelper.decrypt(cryptHelper.sample)
        print(f"Şifreli Mesaj: {cryptHelper.sample}")
        print(f"Çözülmüş Mesaj: {decrypted_example}")

    elif choice == '2':
        message = input("Şifrelemek istediğiniz mesajı girin: ")
        encrypted_message = cryptHelper.encrypt(message)
        print(f"Şifrelenmiş Mesaj: {encrypted_message}")

    elif choice == '3':
        message = input("Şifrelenmiş mesajı girin: ")
        decrypted_message = cryptHelper.decrypt(message)
        print(f"Çözülmüş Mesaj: {decrypted_message}")

    elif choice == '4':
        print("Görüşmek üzere!")
        break
    
    else:
        print("Geçersiz seçenek, lütfen tekrar deneyin..")

    input("\nDevam etmek için herhangi bir tuşa basın...")

    print("\n"+"="*50+"\n")
