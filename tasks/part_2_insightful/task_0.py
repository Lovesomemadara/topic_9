string: str = input()
char: str = input()

char_count: int = 0
for i in string.lower():
    if char == i:
        char_count += 1
if char_count == 0:
    print(False)
else:
    print(char_count)
