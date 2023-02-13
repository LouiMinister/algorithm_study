# 볼링 공 고르기

N, M = map(int, input().split(' '))
category = {n: 0 for n in range(1, M+1)}
res = 0

for i in map(int, input().split(' ')):
    category[i] += 1

vSum = 0
for v in list(category.values())[:-1]:
    vSum += v
    res += v * (N - vSum)

print(res)