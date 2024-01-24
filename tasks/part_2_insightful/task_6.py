line: str = input()

print(len([i for i in line if i.isalpha()]))
print(len([i for i in line if i.isnumeric()]))
print(line.count(' '))

# Лучше решить в итераторе, будет оптимальнее.

count_alpha = 0
for item in line:
    if item.isalpha():
        count_alpha += 1
