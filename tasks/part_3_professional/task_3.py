discount: int = int(input())
prices: list[str, ...] = input().split()

header: list[str, ...] = [
    "Название", "Цена",
    "Сумма скидки", "Новая цена"
]

product: str = 'Товар '

if 0 < discount < 100:
    print('{:<15}{:<10}{:<15}{:<10}'.format(*header))

    for i, price in enumerate(prices, start=1):
        orig_prices: float = float(price)
        disc_amount: float = orig_prices * discount / 100
        new_price: float = orig_prices - disc_amount

        print(f'{product + str(i):<15}{orig_prices:<10.2f}'
              f'{disc_amount:<15.2f}{new_price:<10.2f}')
else:
    print('Размер скидки должен быть больше 0 и не должен превышать 100')
