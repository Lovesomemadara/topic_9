# decimal_ip: int = (int(input()))

# ip: list[str, ...] = []
# for _ in range(4):
#     octet: str = str(decimal_ip % 256)
#     ip.append(octet)
#     decimal_ip = decimal_ip // 256
#
# reversed_ip: list[str, ...] = ip[::-1]
# ip = '.'.join(reversed_ip)
#
# print(ip)
# octets: list[int, ...] = []
# for _ in range(4):
#     first_octet = int()
#     octets.append(int(decimal_ip, 2))
# print(octets)

# Option 2
# ----------------------------------
decimal_ip: int = (int(input()))

binary_octets: str = bin(decimal_ip)[2:].zfill(32)
ip: list[str, ...] = [
    str(int(binary_octets[i:i + 8], 2))
    for i in range(0, 32, 8)
]
ip_address: str = '.'.join(ip)

print(ip_address)
