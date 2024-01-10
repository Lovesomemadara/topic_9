line: str = input()
inp_spr: str = input() or '-'

output: str = ''
length: int = len(line)
for char in range(length):
    if line[char] != inp_spr:
        output += line[char]
        if char != length - 1:
            output += inp_spr
print(output)
