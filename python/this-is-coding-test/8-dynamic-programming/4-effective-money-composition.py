# 효율적인 화폐 구성

N, M = map(int, input().split(' '))
moneys = []
memo = [None] * (M + 1)
memo[0] = 0

for i in range(N):
    moneys.append(int(input()))

for i in range(1, M+1):
    candi = []
    for money in moneys:
        if i-money < 0: continue
        before_cnt = memo[i-money]
        if before_cnt is not None and before_cnt >= 0:
            candi.append(before_cnt+1)
    if len(candi) == 0:
        memo[i] = -1
    else:
        memo[i] = min(candi)

print(memo[M])