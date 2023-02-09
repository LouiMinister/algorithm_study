# 곱하기 혹은 더하기

nums = list(map(int, input()))
res = nums[0]

for num in nums[1:]:
    res = max(res+num, res*num)

print(res)
