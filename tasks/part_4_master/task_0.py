line: list = input().split()

reversed_words = [word[::-1] if len(word) >= 5 else word for word in line]

result: str = ' '.join(reversed_words)

print(result)
