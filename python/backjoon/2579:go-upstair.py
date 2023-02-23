# 계단 오르기
N = int(input())
stair = [0]
for _ in range(N):
    stair.append(int(input()))
if N < 2:
    print(stair[N])
    exit(0)
memo = [0] * (N + 1)
memo[1] = stair[1]
memo[2] = stair[1] + stair[2]

for x in range(3, N+1):
    memo[x] = max(memo[x-2], memo[x-3] + stair[x-1]) + stair[x]

print(memo[N])
