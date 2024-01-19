while True:
    line: str = input('Введите пароль: ')

    if len(line) < 8:
        print('Пароль должен быть минимум 8 символов.')
    elif len(line) > 255:
        print('Пароль не может быть больше 255 символов')
    elif line.isdigit():
        print('Пароль не должен состоять только из цифр.')
    elif not line[-1].isalnum():
        print('Пароль должен заканчиваться буквой или цифрой.')
    elif line[0].isdigit():
        print('Пароль не может начинаться с цифры.')
    elif line.isalpha():
        print('Пароль не должен состоять только из буквенных символов.')
    elif line.isalnum():
        add_special_chars: str = input(
            "ПРЕДУПРЕЖДЕНИЕ: Ваш пароль состоит только из букв и цифр "
            "Хотите добавить специальные символы?(y/n): "
        ).lower()
        if add_special_chars == 'n':
            break
    else:
        break

print('Пароль принят!')
