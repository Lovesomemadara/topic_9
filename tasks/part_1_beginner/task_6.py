stroke: str = input()
even_char: str = ''
odd_char: str = ''
count: int = 0

for i in stroke:
    if count % 2 == 0:
        even_char += i
    else:
        odd_char += i
    count += 1
print(even_char + '\n' + odd_char)
