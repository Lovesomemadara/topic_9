line: str = input()
vowels: str = 'aeiouAEIOUаоуыэеёиюяАОУЫЭЕЁИЮЯ'

print(''.join(['?' if char in vowels else char for char in line]))
