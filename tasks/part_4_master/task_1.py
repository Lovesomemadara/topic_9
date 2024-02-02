order: str = input()

menu: dict = {
    'burger': 'Burger',
    'fries': 'Fries',
    'chicken': 'Chicken',
    'pizza': 'Pizza',
    'sandwich': 'Sandwich',
    'onionrings': 'Onionrings',
    'milkshake': 'Milkshake',
    'coke': 'Coke'
}

result: str = ''
word: str = ''

for char in order:
    word += char
    if word in menu:
        result += menu[word] + ' '
        word = ''

print(result.strip())
