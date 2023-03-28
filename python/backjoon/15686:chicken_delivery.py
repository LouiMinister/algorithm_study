# 치킨 배달

# 0은 빈칸 1은 집 2는 치킨집

# 도시크기 NxN 2<=N<=50
# 1<=M<=13
#
# 시간복잡도: 100 * 13 *(13*12*11*10*9*8) / 6*5*4*3*2*1

# print((100*13*13*12*11*10*9*8)/(6*5*4*3*2))

# ary = [i for i in range(13)]
# comb = list(combinations(ary, 6))
# print(len(comb))
# print((13*12*11*10*9*8)/(6*5*4*3*2))

# 집 별 치킨집
# house[집인덱스] = [(x,y)]
# house_distance[집인덱스] = [(치킨집인덱스, 거리)] 짧은순으로 소팅

from itertools import combinations

N, M = map(int, input().split(' '))
field = [list(map(int, input().split(' '))) for _ in range(N)]
house = []
house_dist = []
chickens = []

for y in range(N):
    for x in range(N):
        if field[y][x] == 2:
            chickens.append((x, y))

for y in range(N):
    for x in range(N):
        if field[y][x] == 1:
            house.append((x, y))
            distances = []
            for c_i, (c_x, c_y) in enumerate(chickens):
                distances.append((c_i, abs(x - c_x) + abs(y - c_y)))
            distances.sort(key=lambda tup: tup[1])
            house_dist.append(distances)

chickens_cnt = len(chickens)
chickens_idx = [i for i in range(chickens_cnt)]
selected_chickens_combs = combinations(chickens_idx, M)

res = 100 * 13
for selected_chickens in selected_chickens_combs:
    cur_res = 0
    # 집 별 치킨집 당 거리
    for distances_on_house in house_dist:
        shortest_distance = 0
        for chicken_idx, distance in distances_on_house:
            if chicken_idx in selected_chickens:
                shortest_distance = distance
                break
        cur_res += shortest_distance
    res = min(res, cur_res)
print(res)

