# 1로 만들기
N = int(input())
dp = [1000000000] * (3 * (N +1))
dp[1] = 0
dp[2] = 1
dp[3] = 1

for i in range(2, N):
    if dp[i] == 0: continue
    dp[i+1] = min(dp[i+1], dp[i] + 1)
    dp[i*2] = min(dp[i*2], dp[i] + 1)
    dp[i*3] = min(dp[i*3], dp[i] + 1)

print(dp[N])