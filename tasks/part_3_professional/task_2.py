print('Программа "Конвертер валют"')

escape: bool = True

while escape:
    print('\nВыберите операцию (0 для выхода):',
          '1. Конвертировать рубли в доллары',
          '2. Конвертировать доллары в рубли', sep='\n')

    num: int = int(input('Введите номер операции: '))
    if num == 0:
        print('До свидания!')
        break
    elif num == 1:
        dol_exchange_rate: float = float(input('Введите курс '
                                               'доллара к рублю: '))
        rub_count: int = int(input('Введите количество рублей: '))
        print(f'Вы получите {dol_exchange_rate * rub_count:.2f} USD')
    elif num == 2:
        rub_exchange_rate: float = float(input('Введите курс '
                                               'рубля к доллару: '))
        dol_count: int = int(input('Введите количество долларов: '))
        print(f'Вы получите {rub_exchange_rate * dol_count:.2f} RUB')
    else:
        print('Неверный выбор операции. Попробуйте ещё раз.')
