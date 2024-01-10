string: str = input().strip()

vowels: str = 'aeiouAEIOUаоуыэеёиюяАОУЫЭЕЁИЮЯ'

final_string: str = ''
for char in string:
    if char in vowels:
        final_string += '?'
    else:
        final_string += char
print(final_string)
