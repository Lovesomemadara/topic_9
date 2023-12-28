line: str = input()
find_char: str = input()

for index, char in enumerate(line):
    if find_char == char:
        print(index)
        break
else:
    print(-1)
