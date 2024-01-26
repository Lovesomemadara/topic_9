line: str = input()

delimeter_count: int = 10
char_length: int = len(line)

print(f'{line:~^{char_length + delimeter_count}}')
