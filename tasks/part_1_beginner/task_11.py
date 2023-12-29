line: str = input()

dot_count: int = 0
digits: str = '0123456789'
is_num: bool = True
for char in line:
    if (
            (char != ' ')
            and (char not in '+-.')
            and (char not in digits)
    ):
        is_num = False
        break

    if char == '.':
        dot_count += 1
        if dot_count > 1:
            is_num = False
            break

print(is_num)
