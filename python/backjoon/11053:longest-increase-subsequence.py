# 가장 긴 증가하는 부분 수열

# N = int(input())
# ary = list(map(int,input().split()))

# 방법 1
# dp = [0] * N
# for i in range(N):
#     max_dp = 0
#     # j = 0 ~ i-1 순회하면서
#     for j in range(i):
#         # ary[j] 가 ary[i] 보다 작은것들 중에 가장 dp[j] 가 큰거 찾아서 dp[i] = 그거 + 1
#         if ary[j] < ary[i]:
#             max_dp = max(max_dp, dp[j])
#     dp[i] = max_dp + 1
# print(max(dp))

# 방법 2
# [100, 50, 70, 90, 75, 87, 105, 78, 110, 60] 이 배열의 LIS를 구한다고 가정해보면,
#
# LIS는 [50, 70, 75, 87, 105, 110] 로, 길이는 6이 된다.
#
# 아래와 같은 순서로 진행된다.
#
# [0]
# [0, 100]
# [0, 50]
# [0, 50, 70]
# [0, 50, 70, 90]
# [0, 50, 70, 75]
# [0, 50, 70, 75, 87]
# [0, 50, 70, 75, 87, 105]
# [0, 50, 70, 75, 78, 105]
#
# [0, 50, 70, 75, 78, 105, 110]
# [0, 50, 60, 75, 78, 105, 110]
#
# 0을 뺀 나머지의 길이를 구하면 LIS의 길이가 된다.

N = int(input())
ary = list(map(int,input().split()))

dp = [ary[0]]
def update(v):
    global dp
    if v > dp[len(dp) - 1]:
        dp.append(v)
    else:
        for i in range(len(dp)):
            if v <= dp[i]:
                dp[i] = v
                return


for i in range(1,N):
    update(ary[i])
print(len(dp))