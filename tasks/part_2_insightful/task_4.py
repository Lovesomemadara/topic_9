string: str = input()

# Option 2
# words: list[str, ...] = string.title().split()
# base_camel_and_pascal: str = ''.join(words)


words: list[str, ...] = string.split()
base_camel_and_pascal: str = ''.join(word.capitalize() for word in words)

camel_case: str = 'camel' + base_camel_and_pascal
pascal_case: str = 'Pascal' + base_camel_and_pascal
snake_case: str = 'snake_' + '_'.join(words).lower()

print(camel_case, pascal_case, snake_case, sep='\n')
