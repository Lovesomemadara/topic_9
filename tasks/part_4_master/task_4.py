text: str = input()
encrypted_text = ''

for char in text:
    if char.isalpha():
        char = char.lower()
        char = chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        opposite_char = chr(ord('a') + ord('z') - ord(char))
        encrypted_text += opposite_char
    elif char.isspace():
        encrypted_text += ' '
    else:
        pass

result = encrypted_text
print(result)
