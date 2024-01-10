string: str = input()

word_count: list[str, ...] = string.split()
print(len(word_count) or False)
