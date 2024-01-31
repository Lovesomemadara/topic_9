HEADER: list[str, ...] = ['Дети до 2-х лет', 'Дети от 3-х до 12 лет',
                          'Взрослые', 'Пенсионеры']

BETWEEN_PRICE: int = 1055
PENSIONERS_PRICE: int = 1449
ADULTS_PRICE: int = 2099
HEAD_TEMPLATE: str = '{:<20}{:<25}{:<20}{:<20}'

ages: list[str, ...] = input(
    'Введите возрасты посетителей через пробел: '
).split()

under_two_count: int = 0
between_age_count: int = 0
adults_count: int = 0
pensioners_count: int = 0

for i, age in enumerate(ages):
    age: int = int(age)
    if age <= 2:
        under_two_count += 1
    if 3 <= age <= 12:
        between_age_count += 1
    if 12 < age < 65:
        adults_count += 1
    if age >= 65:
        pensioners_count += 1

age_rate: list[int, ...] = [under_two_count,
                            between_age_count,
                            adults_count,
                            pensioners_count]

print(HEAD_TEMPLATE.format(*HEADER))
print(HEAD_TEMPLATE.format(*age_rate))

total_cost: int = (
        (between_age_count * BETWEEN_PRICE)
        + (adults_count * ADULTS_PRICE)
        + (pensioners_count * PENSIONERS_PRICE)
)

print(f'\nОбщая стоимость билетов: {total_cost:,}₽')
