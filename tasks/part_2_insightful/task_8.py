line: list[str, ...] = input().split()

max_vowel_count: int = 0
max_vowel_names: list[str, ...] = []

for name in line:
    vowel_count: int = 0
    for char in name:
        if char.lower() in 'aeiouаоуыэеёиюя':
            vowel_count += 1

    if vowel_count > max_vowel_count:
        max_vowel_count = vowel_count
        max_vowel_names = [name]
    elif vowel_count == max_vowel_count:
        max_vowel_names.append(name)
for name in max_vowel_names:
    print(name.capitalize())
