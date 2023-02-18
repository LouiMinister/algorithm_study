# 연구소
from itertools import combinations

H, W = map(int, input().split(' '))
field = []
origin = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def bfs(x, y):
    global field, dx, dy, H, W
    if field[y][x] == 2:
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < W and 0 <= ny < H and field[y+dy[i]][x+dx[i]] == 0:
                field[y + dy[i]][x + dx[i]] = 2
                bfs(x + dx[i], y + dy[i])

def virus():
    global H, W
    for hi in range(H):
        for wi in range(W):
            bfs(wi, hi)

def clear():
    global field, origin, H, W
    field = [[0 for _ in range(W)] for _ in range(H)]
    for hi in range(H):
        for wi in range(W):
            field[hi][wi] = origin[hi][wi]

def count():
    global field, H, W
    res = 0
    for hi in range(H):
        for wi in range(W):
            if field[hi][wi] == 0:
                res += 1
    return res


for i in range(H):
    origin.append(list(map(int, input().split(' '))))

wall_candidate = []
for hi in range(H):
    for wi in range(W):
        if origin[hi][wi] == 0:
            wall_candidate.append((wi, hi))

wall_comb = list(combinations(wall_candidate, 3))

result = 0
result_map = [[0 for _ in range(W)] for _ in range(H)]
for walls in wall_comb:
    clear()
    for wall_x, wall_y in walls:
        field[wall_y][wall_x] = 1
    virus()
    result = max(result, count())
    # if result < count():
    #     result = count()
    #     for hi in range(H):
    #         for wi in range(W):
    #             result_map[hi][wi] = field[hi][wi]

print(result)
# for i in result_map:
#     print(i)

# print(len(wall_comb))

# 7 7
# 2 0 0 0 1 1 0
# 0 0 1 0 1 2 0
# 0 1 1 0 1 0 0
# 0 1 0 0 0 0 0
# 0 0 0 0 0 1 1
# 0 1 0 0 0 0 0
# 0 1 0 0 0 0 0





