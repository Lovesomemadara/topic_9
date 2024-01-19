line: str = input().lower()
char: str = input().lower()

# Option 1
char_count: int = 0
for current_char in line:
    if current_char == char:
        char_count += 1

if not char_count:
    print(False)
else:
    print(char_count)

# Option 2
if char in line:
    print(line.count(char))
else:
    print(False)

# Option 3
print(line.count(char) if char in line else False)
