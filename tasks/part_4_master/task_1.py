MENU: list[str, ...] = [
    'burger', 'fries', 'chicken',
    'pizza', 'sandwich', 'onionrings',
    'milkshake', 'coke'
]

order: str = input()

result: list[str, ...] = []
for item in MENU:
    while item in order:
        result.append(item.capitalize())
        order = order.replace(item, '', 1)

print(' '.join(result))
