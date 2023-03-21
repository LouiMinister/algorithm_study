import math
from itertools import combinations

# 스타트와 링크

# N 명 모이고, N은 짝수. N/2 명으로 팀을 나눠야한다
# 4<=N <=20
# 차이가 최솟값이 되도록. 1<=Sij<=100
#
# 20명중에 10명 찾는건
INF = int(10e20)
N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split(' '))))

# print(*board, sep='\n')
candi = [i for i in range(1, N+1)]
N_half = math.floor(N/2)

comb = list(combinations(candi, N_half))
res = INF
for home in comb:
    away = []
    for i in range(1,N+1):
        if i not in home:
            away.append(i)
    home_score = 0
    away_score = 0
    for i in range(N_half):
        for j in range(N_half):
            home_score += board[home[i] - 1][home[j] - 1]
            away_score += board[away[i] - 1][away[j] - 1]
    score_diff = abs(home_score-away_score)
    res = min(res, score_diff)

print(res)