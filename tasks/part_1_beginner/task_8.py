line: str = input()
nums: str = ''

for char in line:
    if char > nums:
        nums = char
print(ord(nums), nums, sep='\n')
