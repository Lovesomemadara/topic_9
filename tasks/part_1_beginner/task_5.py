'''stroke: str = input()
spr: str = input() or '-'
output = spr.join(stroke)
print(output)'''

stroke: str = input()
inp_spr = input() or '-'
output = ''
for i in range(len(stroke)):
    if stroke[i] != inp_spr:
        output += stroke[i]
        if i != len(stroke) - 1:
            output += inp_spr
print(output)
