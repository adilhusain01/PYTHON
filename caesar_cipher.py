def caesar_cipher(plain_text, shift):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            shifted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            if is_upper:
                shifted_char = shifted_char.upper()
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text

plain_text = input("Enter the plain text: ")
shift = int(input("Enter the number of letters to shift: "))

encrypted_text = caesar_cipher(plain_text, shift)
print("Encrypted text:", encrypted_text)
