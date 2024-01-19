line: str = input()

print(len([i for i in line if i.isalpha()]))
print(len([i for i in line if i.isnumeric()]))
print(line.count(' '))
