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

    # Обработка двойных фамилий
    # surname = '-'.join(part.capitalize() for part in surname.split('-'))

    full_name: str = (f'{counter:0>2} | {surname} '
                      f'{name[0].upper()}.{patronymic[0].upper()}.')
    counter += 1

    names.append(full_name)

print(f'{NUM_SYMBOL:^3}{FIO_SYMBOL:^{max_width}}')
for line in names:
    print(line)
