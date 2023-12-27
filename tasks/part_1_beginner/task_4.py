stroke: str = input()
nums: list = [char for char in stroke if char.isdigit()]

if nums:
    output = ' '.join([digit + '₽' for digit in nums])
else:
    output = False

print(output)
