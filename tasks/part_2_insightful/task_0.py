string: str = input().lower()
char: str = input().lower()

# Option 1
char_count: int = 0
for current_char in string:
    if current_char == char:
        char_count += 1

if not char_count:
    print(False)
else:
    print(char_count)

# Option 2
if char in string:
    print(string.count(char))
else:
    print(False)

# Option 3
print(string.count(char) if char in string else False)
