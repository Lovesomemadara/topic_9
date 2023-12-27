stroke: str = input()
find_char: str = input()

count: int = 0
for i in stroke:
    if i == find_char:
        break
    count += 1
else:
    count = -1
print(count)

for index, char in enumerate(stroke):
    pass
    # https://pythonchik.ru/osnovy/cikl-for-v-python
