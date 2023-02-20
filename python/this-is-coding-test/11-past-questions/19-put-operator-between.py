# 연산자 끼워 넣기

from itertools import permutations

# l = ['A', 'B', 'B', 'C']
# print(list(set(permutations(l, 3))))

N = int(input())
nums = list(map(int, input().split(' ')))
# + - * /
ops_cnt = list(map(int, input().split(' ')))
ops = ['P' for _ in range(ops_cnt[0])] + ['S' for _ in range(ops_cnt[1])] + ['M' for _ in range(ops_cnt[2])] + ['D' for _ in range(ops_cnt[3])]
pmt_ops = list(set(permutations(ops, N-1)))

min_res, max_res = int(10e10), -int(10e10)
for ops_srz in pmt_ops:
    res = nums[0]
    for i in range(N-1):
        if ops_srz[i] == 'P':
            res += nums[i+1]
        if ops_srz[i] == 'S':
            res -= nums[i+1]
        if ops_srz[i] == 'M':
            res *= nums[i + 1]
        if ops_srz[i] == 'D':
            if res * nums[i + 1] < 0:
                res = -(abs(res) // abs(nums[i+1]))
            else:
                res //= nums[i + 1]
    min_res = min(min_res, res)
    max_res = max(max_res, res)

print(max_res)
print(min_res)