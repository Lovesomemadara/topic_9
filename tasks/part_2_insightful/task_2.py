string: str = input()

words: list = string.split('*')
for word in words:
    capitalized_word = word.capitalize()
    print(capitalized_word)
