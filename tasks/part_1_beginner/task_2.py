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
