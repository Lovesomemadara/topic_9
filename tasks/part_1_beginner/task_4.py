line: str = input()

number_found: bool = False
num_list: str = ''

for char in line:
    if ord('0') <= ord(char) <= ord('9'):
        if not number_found:
            num_list = char + '₽ '
            number_found = True
        else:
            num_list += char + '₽ '
else:
    if not number_found:
        print(number_found)

print(num_list)
