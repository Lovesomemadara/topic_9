stroke: str = input()
unique_stroke: str = ''

for i in stroke:
    if i not in unique_stroke:
        unique_stroke += i

print(unique_stroke)
