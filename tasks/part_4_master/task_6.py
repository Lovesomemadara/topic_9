line: str = input()
is_unique: bool = True

for i in range(len(line)):
    for j in range(i + 1, len(line)):
        if line[i] == line[j]:
            is_unique = False
            break

print(is_unique)
