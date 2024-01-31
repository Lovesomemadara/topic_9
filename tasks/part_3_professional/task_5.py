HEADER: list[str, ...] = ['№', 'ФИО']

names: list[str, ...] = []

while True:
    name: str = input().strip()
    if name.lower() == 'end':
        break
    names.append(name)

lines: list[str, ...] = []

for i, name in enumerate(names, start=1):
    initials: str = '.'.join([part[0] for part in name.split()[1:]])
    full_name: str = f'{name.split()[0].capitalize()} {initials.upper()}'
    line: str = f'{i:02} | {full_name}'
    lines.append(line)

print(' {:<9}{:<10}'.format(*HEADER))
for line in lines:
    print(line + '.')

# --------------------------------------------------------

HEADER: list[str, ...] = ['№', 'ФИО']
names: list[str, ...] = []

max_width: int = 0

while True:
    fio: str = input().strip()
    if fio.lower() == 'end':
        break

    surname, name, patronymic = fio.split()
    surname_len: int = len(surname)
    if surname_len > max_width:
        max_width = surname_len

    names.append(fio)

# Вывод
