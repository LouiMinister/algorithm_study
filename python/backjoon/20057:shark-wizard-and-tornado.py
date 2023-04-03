# 마법사 상어와 토네이도
import math

N = int(input())
x, y = math.floor(N/2), math.floor(N/2)
grid = [list(map(int, input().split(' '))) for i in range(N)]
def next_move():
    global N, x, y
    ldru = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    i = 0
    while True:
        for d in range(4):
            if d % 2 == 0: i += 1
            dx, dy = ldru[d]
            to_x, to_y = x + dx * i, y + dy * i
            while not (x == to_x and y == to_y):
                next_x, next_y = x + dx, y + dy
                if next_x == -1: return
                yield (x, y), (next_x, next_y), d
                x, y = next_x, next_y

# 좌하우상. 이동목표기준
def get_sand_percent(direction: int):
    origin_percent = {
        (0, -2): 2,
        (-1, -1): 10,
        (0, -1): 7,
        (1, -1): 1,
        (-2, 0): 5,
        (-1, 1): 10,
        (0, 1): 7,
        (1, 1): 1,
        (0, 2): 2
    }

    if direction == 0: return origin_percent
    elif direction == 1:
        return {(key[1], -key[0]): value for key, value in origin_percent.items()}
    elif direction == 2:
        return {(-key[0], -key[1]): value for key, value in origin_percent.items()}
    elif direction == 3:
        return {(-key[1], key[0]): value for key, value in origin_percent.items()}

def sand_move(x1, y1, x2, y2, d):
    global grid
    ldru = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    sand_percent = get_sand_percent(d)
    cur_sand = grid[y2][x2]
    left_sand = cur_sand
    grid[y2][x2] = 0
    # 각 좌표별 모래량, 남은 모래량 업데이트, 각 좌표에 모래 업데이트
    for (dx, dy), percent in sand_percent.items():
        x, y = x2 + dx, y2 + dy
        sand = math.floor(cur_sand / 100 * percent)
        left_sand -= sand
        if 0 <= x < N and 0 <= y < N:
           grid[y][x] += sand
    left_x, left_y = x2 + ldru[d][0], y2 + ldru[d][1]
    if 0 <= left_x < N and 0 <= left_y < N:
        grid[left_y][left_x] += left_sand

total_score = 0
for i in range(N):
    for j in range(N):
        total_score += grid[i][j]

for (x1, y1), (x2, y2), d  in next_move():
    sand_move(x1, y1, x2, y2, d)


for i in range(N):
    for j in range(N):
        total_score -= grid[i][j]

print(total_score)


# 5
# 100 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0