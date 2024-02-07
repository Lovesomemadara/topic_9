decimal_ip: int = (int(input()))

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

binary_octets: str = bin(decimal_ip)[2:]
sub_octets = [
    binary_octets[i:i+8]
    for i in range
    (0, len(binary_octets), 8)
]

ip = [int(sub_octet, 2) for sub_octet in sub_octets]

joined_string = '.'.join([str(number) for number in ip])

print(joined_string)
