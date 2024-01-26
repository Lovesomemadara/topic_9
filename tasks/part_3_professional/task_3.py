discount: int = int(input())
prices: list[str, ...] = input().split()

header: list[str, ...] = [
    "Название", "Цена",
    "Сумма скидки", "Новая цена"
]

if 0 < discount < 100:
    print('{:<15} {:<10} {:<15} {:<10}'.format(*header))

    # 1. Не соответствует вывод (знаки после запятой).
    for i, price in enumerate(prices, start=1):
        orig_prices: float = float(price)
        disc_amount: float = orig_prices * discount / 100
        new_price: float = orig_prices - disc_amount

        print(f'Товар {i:<15}{orig_prices:<10} '
              f'{disc_amount:<15} {new_price:<10}')
else:
    print('Размер скидки должен быть больше 0 и не должен превышать 100')
