ip: list = input().split('.')

decimal_ip: int = 0
error_flag: bool = False
for num in ip:
    if 0 <= int(num) <= 255:
        decimal_ip = (decimal_ip * 256) + int(num)
    else:
        error_flag = True
        print('Одно из чисел, либо меньше 0, либо больше 255!')
        break

if not error_flag:
    print(decimal_ip)

# ------------------------------------

# bin()[2:]
# int('1001', 2)
for num in ip:
    pass

