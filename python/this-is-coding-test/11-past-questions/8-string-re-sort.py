inputs = list(input())
chars = []
nums = 0
for c in inputs:
    if c.isalpha():
        chars.append(c)
    else:
        nums += int(c)
chars.sort()
chars.append(str(nums))
res = ''.join(chars)
print(res)
