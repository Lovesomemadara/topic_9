text: str = input().lower()

encrypted_text: str = ''
for char in text:
    if char.isalpha():
        # char = chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        # opposite_char = chr(ord('a') + ord('z') - ord(char))

        char = chr(ord('z') - ((ord(char) - ord('a')) + 13) % 26)
        encrypted_text += char

    elif char.isspace():
        encrypted_text += char

print(encrypted_text)
