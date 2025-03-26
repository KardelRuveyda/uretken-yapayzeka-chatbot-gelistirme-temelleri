def decoder(text):
    text_decoded = ""
    i=0
    while i<len(text):
        char=text[i]
        if char.isalpha():
            if char.islower():
                temp = chr(((ord(char) - ord('a') - 5) % 26) + ord('a'))
            else:
                temp = chr(((ord(char) - ord('A') - 5) % 26) + ord('A'))
            text_decoded += temp
            i+=1
        elif char.isdigit():
            temp=""
            while 1:
                char = text[i]
                temp += char
                i+=1
                if i == len(text) or not text[i].isnumeric():
                    break
            text_decoded += temp[::-1]
        else:
            text_decoded += char
            i+=1
            continue
    return text_decoded
text_decoded =decoder("ymj vznhp 123 gwtbs ktc ozrux tajw ymj qfed itl")
print(text_decoded)