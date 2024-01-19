line: str = input()

word_count: list[str, ...] = line.split()
print(len(word_count) or False)
