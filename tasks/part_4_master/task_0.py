line: list[str, ...] = input().split()

reversed_words: list[str, ...] = [
    word[::-1] if len(word) >= 5 else word for word in line
]

result: str = ' '.join(reversed_words)

print(result)

# Option 2
# -------------------------

for i in range(len(line)):
    if len(line[i]) >= 5:
        line[i] = line[i][::-1]

print(' '.join(line))
