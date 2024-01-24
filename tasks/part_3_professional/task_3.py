discount: int = int(input())
prices: list = list(map(float, input().split()))

header: list[str, ...] = ["Название", "Цена",
                          "Сумма скидки", "Новая цена"]

if 0 < discount < 100:
    print('{:<15} {:<10} {:<15} {:<10}'.format(*header))
    for i, price in enumerate(prices):
        orig_prices: float = float(f'{price:.2f}')
        disc_amount: float = float(f'{price * discount / 100:.2f}')
        new_price: float = float(f'{price - (price / discount / 100):.2f}')
        print(f'Товар {i+1:<10}{orig_prices:<10} '
              f'{disc_amount:<15} {new_price:<15}')
else:
    print('Размер скидки должен быть больше 0 и не должен превышать 100')
