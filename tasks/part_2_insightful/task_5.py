string: str = input().strip()

vowels: str = 'aeiouAEIOUаоуыэеёиюяАОУЫЭЕЁИЮЯ'

final_string: str = ''
for char in range(len(string)):
    if string[char] in vowels:
        final_string += '?'
    else:
        final_string += string[char]
print(final_string)
