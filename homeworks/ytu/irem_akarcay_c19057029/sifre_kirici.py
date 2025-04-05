# sifre_kirici.py

import re

def shift_char(ch, shift):
    """
    Verilen harfi 'shift' kadar kaydırır.
    Küçük/büyük harf ayrımı yapar.
    Harf değilse olduğu gibi döndürür.
    """
    if ch.islower():
        return chr(((ord(ch) - ord('a') + shift) % 26) + ord('a'))
    elif ch.isupper():
        return chr(((ord(ch) - ord('A') + shift) % 26) + ord('A'))
    else:
        return ch

def reverse_numbers(text):
    """
    Metindeki tüm sayı dizilerini ters çevirir.
    Örnek: 'abc123de45' → 'abc321de54'
    """
    return re.sub(r'\d+', lambda m: m.group(0)[::-1], text)

def encrypt_message(text, shift):
    """
    Mesajı şifreler:
    - Harfleri shift kadar ileri kaydırır.
    - Sayıları ters çevirir.
    """
    shifted = ''.join(shift_char(ch, shift) for ch in text)
    return reverse_numbers(shifted)

def decrypt_message(text, shift):
    """
    Şifreyi çözer:
    - Sayıları ters çevirerek orijinal hale getirir.
    - Harfleri shift kadar geri kaydırır.
    """
    reversed_text = reverse_numbers(text)
    return ''.join(shift_char(ch, -shift) for ch in reversed_text)

# Demo
#The if condition was evaluating to false, and never running the code below it
#Changing the condition from _name_ to __name__ fixes the issue in a notebook
if __name__ == "__main__":
    encrypted_msg = "ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl"
    print("Şifreli Mesaj   :", encrypted_msg)
    
    default_shift = 5
    decrypted = decrypt_message(encrypted_msg, shift=default_shift)
    print("Çözülmüş Mesaj  :", decrypted)

    # Kullanıcıdan mesaj ve şifreleme seviyesi al
    user_msg = input("\nŞifrelemek istediğiniz mesajı girin: ")
    
    try:
        shift_val = int(input("Kaç karakter kaydırılsın? (örn: 3, 5, 13): "))
    except ValueError:
        print("Geçersiz sayı girdiniz. Varsayılan olarak 5 kullanılacak.")
        shift_val = 5

    encrypted_user_msg = encrypt_message(user_msg, shift=shift_val)
    decrypted_user_msg = decrypt_message(encrypted_user_msg, shift=shift_val)

    print("\nŞifrelenmiş     :", encrypted_user_msg)
    print("Şifre Çözümü    :", decrypted_user_msg)