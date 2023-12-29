line: str = input()

max_char: str = ''
for curr_char in line:
    if curr_char > max_char:
        max_char = curr_char
print(ord(max_char), max_char, sep='\n')
