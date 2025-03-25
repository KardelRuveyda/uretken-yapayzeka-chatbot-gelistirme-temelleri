def decrypt_message(encrypted_text):
    decrypted_text = ""
    temp_number = ""

    for char in encrypted_text:
        if char.isalpha():
            shift = -5  # 5 harf geri kaydır
            if char.islower():
                decrypted_text += chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
            else:
                decrypted_text += chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
        elif char.isdigit():
            temp_number += char  # Sayıları biriktir
        else:
            if temp_number:
                decrypted_text += temp_number[::-1]  # Sayıyı tekrar ters çevir
                temp_number = ""  # Sayı hafızasını sıfırla
            decrypted_text += char  # Boşlukları ve noktalama işaretlerini koru

    if temp_number:
        decrypted_text += temp_number[::-1]  # Son sayıyı ekle

    return decrypted_text


# Örnek şifreli mesajın decryptionı
encrypted_message = "ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl"
original_message = decrypt_message(encrypted_message)

print("Çözülmemiş Mesaj:", encrypted_message)
print("Çözülmüş Mesaj:", original_message)


"""Bonus"""


def encrypt_message(text):
    encrypted_text = ""
    temp_number = ""

    for char in text:
        if char.isalpha():
            shift = 5  # 5 harf ileri kaydır
            if char.islower():
                encrypted_text += chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
            else:
                encrypted_text += chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
        elif char.isdigit():
            temp_number += char  # Sayıları biriktir
        else:
            if temp_number:
                encrypted_text += temp_number[::-1]  # Sayıyı ters çevir
                temp_number = ""  # Sayı hafızasını sıfırla
            encrypted_text += char  # Boşlukları ve noktalama işaretlerini koru

    if temp_number:
        encrypted_text += temp_number[::-1]  # Son sayıyı ekle

    return encrypted_text


# Menü
while True:
    print("\nProgramı Rakamları Girerek Çalıştır")
    print("1- Şifrele")
    print("2- Şifre Çöz")

    choice = input("İşlemin numarasını girin\n")

    if choice == "1":
        message = input("\nŞifrelenecek metin: ")
        encrypted = encrypt_message(message)
        print("Sonuç:", encrypted)

    elif choice == "2":
        encrypted_message = input("\nÇözülecek metin: ")
        decrypted = decrypt_message(encrypted_message)
        print("Sonuç:", decrypted)
