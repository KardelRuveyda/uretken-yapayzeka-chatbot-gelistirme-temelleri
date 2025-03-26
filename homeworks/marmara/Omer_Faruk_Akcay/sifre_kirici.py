def code(string):
    new_string = ""
    buffer = ""
    
    for char in string:
        # hash yapısı ile z den sonra a gelmesi sağlanır
        # a -> 97 z -> 122 | 122 - 96 = 26 harf
        if "a" <= char <= "z":
            new_char = chr((ord(char) - ord("a") + 5) % 26 + ord("a"))
            new_string += buffer[::-1]
            buffer = ""
            new_string += new_char
        
        # a -> 65 z -> 90 | 90 - 64 = 26 harf
        elif "A" <= char <= "Z":
            new_char = chr((ord(char) - ord("A") + 5) % 26 + ord("A"))
            new_string += buffer[::-1]
            buffer = ""
            new_string += new_char

        # sayılar grup grup şekilde bufferda saklanır
        elif char.isdigit():
            buffer += char

        # diğer karakterler degismesin
        else:
            new_string += char
    
    new_string += buffer[::-1] 
    return new_string

def decode(string):
    new_string = ""
    buffer = ""
    
    for char in string:
        # hash yapısı ile z den sonra a gelmesi sağlanır
        # a -> 97 z -> 122 | 122 - 96 = 26 harf
        if "a" <= char <= "z":
            new_char = chr((ord(char) - ord("a") - 5) % 26 + ord("a"))
            new_string += buffer[::-1]
            buffer = ""
            new_string += new_char
        
        # a -> 65 z -> 90 | 90 - 64 = 26 harf
        elif "A" <= char <= "Z":
            new_char = chr((ord(char) - ord("A") - 5) % 26 + ord("A"))
            new_string += buffer[::-1]
            buffer = ""
            new_string += new_char

        # sayılar grup grup şekilde bufferda saklanır
        elif char.isdigit():
            buffer += char

        # diğer karakterler degismesin
        else:
            new_string += char
    
    new_string += buffer[::-1] 
    return new_string

string = "merhabalar"
encoded_string = code(string)
decoded_string = decode(encoded_string)

print("Program basladi!\n")
print("Deneme stringi:", string)
print("Sifrelenmis deneme stringi:", encoded_string)
print("Cozulmus deneme stringi:", decoded_string, "\n")

test_string = "ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl"
real_string = decode(test_string)

print("Verilen sifrelenmis test stringi:", test_string)
print("Test stringinin cozulmus hali:", real_string, "\n")

