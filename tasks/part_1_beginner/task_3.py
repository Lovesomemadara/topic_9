stroke: str = input()

is_printed: bool = False

for i in range(len(stroke)):
    if stroke[i] == ' ':
        continue
    substring = stroke[:i + 1]
    print(substring)
