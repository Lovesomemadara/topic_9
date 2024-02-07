pascal_case: str = input().strip()
result: str = pascal_case[0].lower()

for char in range(1, len(pascal_case)):
    if pascal_case[char].isupper():
        result += '_' + pascal_case[char].lower()
    else:
        result += pascal_case[char]

print(result)
