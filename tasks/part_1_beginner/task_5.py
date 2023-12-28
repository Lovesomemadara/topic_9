line: str = input()
inp_spr = input() or '-'

output = ''
count: int = len(line)
for char in range(count):
    if line[char] != inp_spr:
        output += line[char]
        if char != count - 1:
            output += inp_spr
print(output)
