import re

def decrypt_message(message):
	decrypted = ""

	for char in message:
		if char.isalpha():
			base = ord('A') if char.isupper() else ord('a')
			shifted = (ord(char) - base - 5) % 26 + base
			decrypted += chr(shifted)
		elif char.isdigit():
			decrypted += char
		else:
			decrypted += char

	def reverse_number(match):
		return match.group()[::-1]

	decrypted = re.sub(r'\d+', reverse_number, decrypted)

	return decrypted

msg = "ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl"
print(decrypt_message(msg))
