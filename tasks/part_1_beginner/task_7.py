start_word: str = input()
end_word: str = ''

for i in start_word:
    end_word = start_word[::-1]
if start_word == end_word:
    print(True)
else:
    print(False)
