line: str = input().strip()

vowels: str = 'aeiouAEIOUаоуыэеёиюяАОУЫЭЕЁИЮЯ'
replace: str = '?' * 30

correct_line: dict[int, str | None] = line.maketrans(vowels, replace)

print(line.translate(correct_line))
