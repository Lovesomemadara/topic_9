line: str = input()
vowels: str = 'aeiouAEIOUаоуыэеёиюяАОУЫЭЕЁИЮЯ'
replace: str = '?' * 30
remove: str = 'T'

print(''.join(['?' if char in vowels else char for char in line]))
