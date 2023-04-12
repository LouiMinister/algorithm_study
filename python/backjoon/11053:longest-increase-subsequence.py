# 가장 긴 증가하는 부분 수열

N = int(input())
ary = list(map(int,input().split()))

dp = [0] * N
for i in range(N):
    max_dp = 0
    # j = 0 ~ i-1 순회하면서
    for j in range(i):
        # ary[j] 가 ary[i] 보다 작은것들 중에 가장 dp[j] 가 큰거 찾아서 dp[i] = 그거 + 1
        if ary[j] < ary[i]:
            max_dp = max(max_dp, dp[j])
    dp[i] = max_dp + 1
print(max(dp))