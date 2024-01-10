line: str = input()

number_found: bool = False
# digits: str = '0123456789'
num_list: str = ''
for char in line:
    if ord('0') <= ord(char) <= ord('9'):
    # if char in digits:
        number_found = True
        num_list += char + '₽ '

if not number_found:
    print(number_found)
else:
    print(num_list)
