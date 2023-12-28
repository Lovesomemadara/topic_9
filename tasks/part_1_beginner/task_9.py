is_word: bool = False
word_count: int = 0
for char in input():
    if char == ' ':
        is_word = False
    elif not is_word:
        is_word = True
        word_count += 1
print(word_count)
