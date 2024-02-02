decimal_ip: int = (int(input()))

ip: str = ''
for _ in range(4):
    octet: str = str(decimal_ip % 256)
    ip = octet + '.' + ip
    decimal_ip = decimal_ip // 256

ip = ip.rstrip('.')  # лучше использовать join.

print(ip)
