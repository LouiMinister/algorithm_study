# 바닥 공사

N = int(input())

memo = [0, 1, 3] + [None] * (N - 2)

for i in range(3, N+1):
    memo[i] = (memo[i-1] + memo[i-2] * 2) % 79679

print(memo[N])