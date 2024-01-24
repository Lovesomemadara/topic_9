print('Программа "Конвертер валют"')

while True:
    print('\nВыберите операцию (0 для выхода):',
          '1. Конвертировать рубли в доллары',
          '2. Конвертировать доллары в рубли', sep='\n')

    num: str = input('Введите номер операции: ').strip()

    if not num.isdigit():
        print('Введите числовое значение, номер операции')
        continue

    if num == '0':
        print('До свидания!')
        break

    if num not in ('1', '2'):
        print('Неверный выбор операции. Попробуйте ещё раз.')
        continue

    rate_hint: str = 'Введите курс доллара к рублю: '
    currency_hint: str = 'Введите количество рублей: '
    sign: str = 'USD'

    if num == '2':
        rate_hint: str = 'Введите курс рубля к доллару: '
        currency_hint: str = 'Введите количество долларов: '
        sign: str = 'RUB'

    exchange_rate: float = float(input(rate_hint))
    currency_amount: float = float(input(currency_hint))

    print(f'Вы получите {exchange_rate * currency_amount:0>5.2f} {sign}')
