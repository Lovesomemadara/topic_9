line: str = input()

unique_chars: str = ''
for char in line:
    if char not in unique_chars:
        unique_chars += char

print(unique_chars)
