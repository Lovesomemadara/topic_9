stroke: str = input()

for i in range(len(stroke)):
    if stroke[i] == ' ':
        continue
    substring = stroke[:i + 1]
    print(substring)
