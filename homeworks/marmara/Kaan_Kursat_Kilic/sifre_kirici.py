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
    print("Mesaj Sifreleme / Sifre Cozme Programi")
    print("Yapmak istediginiz islemi secin:")
    print("1 - Sifre Coz")
    print("2 - Mesaj Sifrele")

    choice = input("Seciminiz (1/2): ").strip()

    if choice == '1':
        encrypted = input("Sifrelenmis mesaji girin: ").strip()
        decrypted = decrypt_message(encrypted)
        print("Cozulmus mesaj:\n", decrypted)
    elif choice == '2':
        plain = input("Sifrelenecek mesaji girin: ").strip()
        encrypted = encrypt_message(plain)
        print("Sifrelenmis mesaj:\n", encrypted)
    else:
        print("Gecersiz secim. Lutfen 1 veya 2 girin.")

if __name__ == "__main__":
    main()
