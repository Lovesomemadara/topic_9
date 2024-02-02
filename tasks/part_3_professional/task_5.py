# HEADER: list[str, ...] = ['№', 'ФИО']
#
# names: list[str, ...] = []
#
# while True:
#     name: str = input().strip()
#     if name.lower() == 'end':
#         break
#     names.append(name)
#
# lines: list[str, ...] = []
#
# for i, name in enumerate(names, start=1):
#     initials: str = '.'.join([part[0] for part in name.split()[1:]])
#     full_name: str = f'{name.split()[0].capitalize()} {initials.upper()}'
#     line: str = f'{i:02} | {full_name}'
#     lines.append(line)
#
# print(' {:<9}{:<10}'.format(*HEADER))
# for line in lines:
#     print(line + '.')

# --------------------------------------------------------

HEADER: list[str, ...] = ['№', 'ФИО']
NUM_SYMBOL: str = '№'
FIO_SYMBOL: str = 'ФИО'
names: list[str, ...] = []

max_width: int = 0
counter: int = 1
while True:
    fio: str = input().strip()
    if fio.lower() == 'end':
        break

    surname, name, patronymic = fio.split()
    surname_len: int = len(surname)
    if surname_len > max_width:
        max_width = surname_len

    full_name: str = (f'{counter:0>2} | {surname.capitalize()} '
                      f'{name[0].upper()}.{patronymic[0].upper()}.')
    counter += 1

    names.append(full_name)

print(f'{NUM_SYMBOL:^3}{FIO_SYMBOL:^{max_width}}')
for line in names:
    print(line)
