line: str = input()

dot_count: int = 0
is_num: bool = True
for char in line:
    if char == '+' or char == '-' or char == ' ':
        line = line[1:]
        continue
    if char == '.':
        dot_count += 1
        if dot_count > 1:
            is_num = False
            break
    else:
        if ord('0') <= ord(char) <= ord('9'):
            is_num = True
        else:
            is_num = False
print(is_num)






