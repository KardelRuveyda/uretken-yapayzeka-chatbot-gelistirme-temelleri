def shift_char(char, shift):
    if char.isalpha():
        ascii_offset = ord('A') if char.isupper() else ord('a')
        return chr(ascii_offset + (ord(char) - ascii_offset + shift) % 26)
    return char

def reverse_string(s):
    #sayıları ters çevirmek için
    return s[::-1]

def process_message(message, shift):
    """
    Hem şifreleme hem de deşifreleme için ortak fonksiyon.
    Harfleri kaydirir, sayilari ters çevirir ve diğer karakterleri korur.
    """
    result = []
    number_buffer = []
    
    for char in message:
        if char.isalpha():
            result.append(shift_char(char, shift))
        elif char.isdigit():
            number_buffer.append(char)
        else:
            if number_buffer:
                result.append(reverse_string(''.join(number_buffer)))  # Biriken sayıları ters çevirme
                number_buffer = []
            result.append(char)  # Boşluk ve noktalama işaretlerini ekleme
    
    if number_buffer:
        result.append(reverse_string(''.join(number_buffer)))
    
    return ''.join(result)

def encrypt_message(message):
    # Harfleri 5 ileri kaydirir, sayilari ters çevirir
    return process_message(message, 5)

def decrypt_message(encrypted_message):
    #Harfleri 5 geri kaydirir, sayilari ters çevirir
    return process_message(encrypted_message, -5)

def main():
    
    while True:
        print("\nSifreleme Uygulaması")
        print("\n1. Mesaj Şifrele")
        print("2. Mesaj Çöz")
        print("3. Çıkış!")
        
        choice = input("\nSeçiminizi giriniz (1-3): ")
        
        if choice == "1":
            message = input("Şifrelenecek mesajı giriniz: ")
            print("Şifrelenmiş mesaj:", encrypt_message(message))
        elif choice == "2":
            message = input("Çözülecek mesajı giriniz: ")
            print("Çözülmüş mesaj:", decrypt_message(message))
        elif choice == "3":
            print("Program sonlandırılıyor.")
            break
        else:
            print("Geçersiz seçim! Lütfen 1-3 arasında bir sayı girin.")

if __name__ == "__main__":
    main()
