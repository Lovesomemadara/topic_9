line: str = input()

count_alpha: int = 0
count_num: int = 0
space_count: int = 0
for item in line:
    if item.isalpha():
        count_alpha += 1
    if item.isnumeric():
        count_num += 1
    if item.isspace():
        space_count += 1
print(count_alpha, count_num, space_count, sep='\n')
