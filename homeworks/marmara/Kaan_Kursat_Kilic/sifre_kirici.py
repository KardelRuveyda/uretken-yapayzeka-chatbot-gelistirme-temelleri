def shift_char(c, shift):

    if c.isalpha():
        base = ord('a')
        return chr((ord(c) - base + shift) % 26 + base)
    else:
        return c

def decrypt_message(message):

    return ''.join(shift_char(c, -5) for c in message)

def encrypt_message(message):

    return ''.join(shift_char(c, 5) for c in message)

def main():
    print("Mesaj Şifreleme / Şifre Çözme Programı")
    print("Yapmak istediğiniz işlemi seçin:")
    print("1 - Şifre Çöz")
    print("2 - Mesaj Şifrele")

    choice = input("Seçiminiz (1/2): ").strip()

    if choice == '1':
        encrypted = input("Şifrelenmiş mesajı girin: ").strip()
        decrypted = decrypt_message(encrypted)
        print("Çözülmüş mesaj:\n", decrypted)
    elif choice == '2':
        plain = input("Şifrelenecek mesajı girin: ").strip()
        encrypted = encrypt_message(plain)
        print("Şifrelenmiş mesaj:\n", encrypted)
    else:
        print("Geçersiz seçim. Lütfen 1 veya 2 girin.")

if __name__ == "__main__":
    main()
