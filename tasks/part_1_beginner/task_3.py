line: str = input()

final_line: str = ''
is_printed: bool = False
for char in line:
    if is_printed or char != ' ':
        is_printed = True
        final_line += char
        print(final_line)
