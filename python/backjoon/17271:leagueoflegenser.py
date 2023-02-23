# 리그 오브 레전설

T, C = map(int, input().split(' '))
dp = [1 for i in range(0,C)] + [None] * (T+1)

for i in range(C, T+1):
    dp[i] = (dp[i-1] + dp[i-C]) % 1000000007

print(dp[T])