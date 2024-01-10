string: str = input()

words: list = string.split()
camel_case: str = ''.join(word.capitalize() for word in words)
pascal_case: str = ''.join(word.capitalize() for word in words)
snake_case: str = '_'.join(words).lower()

print('camel' + camel_case,
      'Pascal' + pascal_case,
      'snake_' + snake_case, sep='\n')
