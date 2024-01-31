HEADER: list[str, ...] = ['№', 'ФИО']

names: list[str, ...] = []

while True:
    name: str = input().strip()
    if name.lower() == 'end':
        break
    names.append(name)

lines: list[str, ...] = []

for i, name in enumerate(names, 1):
    initials: str = '.'.join([part[0] for part in name.split()[1:]])
    full_name: str = f'{name.split()[-1].capitalize()} {initials.upper()}'
    line: str = f'{i:02} | {full_name}'
    lines.append(line)

print(' {:<9}{:<10}'.format(*HEADER))
for line in lines:
    print(line + '.')
