header: list[str, ...] = ['Дети до 2-х лет', 'Дети от 3-х до 12 лет',
                          'Взрослые', 'Пенсионеры']

ages: list[int, ...] = (list
                        (map
                         (int, input('Введите возрасты '
                                     'посетителей через пробел: ').split()))
                        )

under_two_count: int = 0
between_age_count: int = 0
adults_count: int = 0
pensioners_count: int = 0

print('{:<20}{:<25}{:<20}{:<20}'.format(*header))

for i, age in enumerate(ages):
    if age <= 2:
        under_two_count += 1
    if 3 <= age <= 12:
        between_age_count += 1
    if 12 < age < 65:
        adults_count += 1
    if age >= 65:
        pensioners_count += 1

print(f'{under_two_count:<20}{between_age_count:<25}'
      f'{adults_count:<20}{pensioners_count:<20}')

print(f'\nОбщая стоимость билетов: '
      f'{(between_age_count * 1055) + (adults_count * 2099) + (pensioners_count * 1449):,.0f}₽')
