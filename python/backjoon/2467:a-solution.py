# 용액
from itertools import combinations

N = int(input())
slts = list(map(int, input().split(' ')))
l_idx, r_idx = 0, len(slts) - 1

res = (0,0)
min_sum = 2123123123
while l_idx < r_idx:
    if abs(slts[l_idx] + slts[r_idx]) < min_sum:
        min_sum = abs(slts[l_idx] + slts[r_idx])
        res = (slts[l_idx], slts[r_idx])
    if abs(slts[l_idx + 1] + slts[r_idx]) < abs(slts[l_idx] + slts[r_idx - 1]):
        l_idx += 1
    else:
        r_idx -= 1
print(*res)