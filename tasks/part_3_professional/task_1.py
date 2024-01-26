line: str = input()

delimiter: str = '~' * 5

print(f'{line:~^{len(line) + len(delimiter) * 2}}')
