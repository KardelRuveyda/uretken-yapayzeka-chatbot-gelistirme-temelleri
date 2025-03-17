def encrypt_message(message):
    result = ""
    number_buffer = ""
    
    for char in message:
        if char.isalpha():
            # Eğer karakter küçük harfse 'a' (97), büyük harfse 'A' (65) ASCII değerini alır
            ascii_offset = ord('a') if char.islower() else ord('A')
            
            # Karakterin alfabedeki pozisyonunu bulup 5 harf ileri kaydırır
            # % 26 ile z'den sonra başa dönmesini sağlar
            shifted = (ord(char) - ascii_offset + 5) % 26
            
            # Yeni pozisyonu tekrar ASCII karakterine çevirir
            result += chr(ascii_offset + shifted)
        elif char.isdigit():
            # Sayıyı buffer'a ekle
            number_buffer += char
        else:
            # Eğer buffer'da sayı varsa, ters çevirip ekle
            if number_buffer:
                result += number_buffer[::-1]
                number_buffer = ""
            # Boşlukları ve noktalama işaretlerini olduğu gibi bırak
            result += char
    
    # Son sayıyı kontrol et
    if number_buffer:
        result += number_buffer[::-1]
    
    return result

def decrypt_message(encrypted_message):
    result = ""
    number_buffer = ""
    
    for char in encrypted_message:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            shifted = (ord(char) - ascii_offset - 5) % 26
            result += chr(ascii_offset + shifted)
        elif char.isdigit():
            number_buffer += char
        else:
            if number_buffer:
                result += number_buffer[::-1]
                number_buffer = ""
            result += char
    
    if number_buffer:
        result += number_buffer[::-1]
    
    return result

def main():
    # Problemde verilen şifrelenmiş mesaj
    encrypted = "ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl"
    
    print("Şifrelenmiş mesaj:", encrypted)
    print("Çözülmüş mesaj:", decrypt_message(encrypted))
    
    while True:
        print("\n1. Mesaj Şifrele")
        print("2. Mesaj Çöz")
        print("3. Çıkış")
        
        choice = input("\nSeçiminiz (1-3): ")
        
        if choice == "1":
            message = input("Şifrelenecek mesajı girin: ")
            encrypted = encrypt_message(message)
            print("Şifrelenmiş mesaj:", encrypted)
        elif choice == "2":
            message = input("Çözülecek mesajı girin: ")
            decrypted = decrypt_message(message)
            print("Çözülmüş mesaj:", decrypted)
        elif choice == "3":
            print("Program sonlandırılıyor...")
            break
        else:
            print("Geçersiz seçim! Lütfen 1-3 arasında bir sayı girin.")

if __name__ == "__main__":
    main()