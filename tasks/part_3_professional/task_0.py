line: str = input().lower()
vowels: str = 'aeiouаоуыэеёиюя'

vowels_count: int = len([char for char in line if char in vowels])

print(f'Отношение гласных: {float(vowels_count / len(line) * 100):.2f}%')
