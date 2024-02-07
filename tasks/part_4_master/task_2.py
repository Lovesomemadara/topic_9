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

# Option 2
# ------------------------------------

ip: list = input().split('.')
decimal_ip: int = 0
octets: str = ''
for num in ip:
    num = int(num)
    octets += str(bin(num)[2:]).zfill(8)
    decimal_ip = int(octets, 2)
print(decimal_ip)
