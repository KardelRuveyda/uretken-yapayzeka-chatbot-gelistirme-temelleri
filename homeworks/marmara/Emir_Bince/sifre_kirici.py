def caesar_cipher(shift: int, text: str, mode: str) -> str:
    chars = "abcdefghijklmnopqrstuvwxyz"
    shift = shift % len(chars)
    if mode.strip().lower() == "decipher":
        shift = -shift
    
    result_list = []
    for char in text:
        if char.lower() in chars:
            new_char = chars[(chars.index(char.lower()) + shift) % len(chars)]
            result_list.append(new_char.upper() if char.isupper() else new_char)
        else:
            result_list.append(char)
    
    reversed_result = []
    number_buffer = []
    for char in result_list:
        if char.isdigit():
            number_buffer.append(char)
        else:
            reversed_result.extend(reversed(number_buffer))
            number_buffer = []
            reversed_result.append(char)

    reversed_result.extend(reversed(number_buffer))
    
    return "".join(reversed_result)


if __name__ == "__main__":
    message = "The quick brown fox jumps over the lazy dog in 2077!"
    shift = 5
    mode = "cipher"

    encrypted_message = caesar_cipher(shift, message, mode)

    print(f"encrypted message: {encrypted_message}")
    print(f"decrypted message: {caesar_cipher(shift, encrypted_message, 'decipher')}")