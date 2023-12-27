stroke: str = input()
nums: list = []

for i in stroke:
    nums.append(ord(i))
print(max(nums))
