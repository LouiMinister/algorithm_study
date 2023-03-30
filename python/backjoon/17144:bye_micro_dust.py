# 미세먼지 안녕!
import math

mis = lambda : map(int, input().split(' '))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
H, W, T = mis()
grid = []
machine =[]
for h_i in range(H):
    row = list(mis())
    grid.append(row)
    for w_i in range(W):
        if row[w_i] == -1:
            machine.append((w_i, h_i))

def up_machine():
    global machine, grid
    machine_x, machine_y = machine[0]
    cur_x, cur_y = machine[0]
    while cur_y -1 >= 0:
        grid[cur_y][cur_x] = grid[cur_y - 1][cur_x] if cur_y != machine_y else -1
        cur_y -= 1
    while cur_x + 1 < W:
        grid[cur_y][cur_x] = grid[cur_y][cur_x+1]
        cur_x += 1
    while cur_y + 1 <= machine_y:
        grid[cur_y][cur_x] = grid[cur_y + 1][cur_x]
        cur_y += 1
    while cur_x - 1 >= 0:
        grid[cur_y][cur_x] = grid[cur_y][cur_x-1] if cur_x-1 != machine_x else 0
        cur_x -= 1

def down_machine():
    global machine, grid
    machine_x, machine_y = machine[1]
    cur_x, cur_y = machine[1]
    while cur_y + 1 < H:
        grid[cur_y][cur_x] = grid[cur_y + 1][cur_x] if cur_y != machine_y else -1
        cur_y += 1
    while cur_x + 1 < W:
        grid[cur_y][cur_x] = grid[cur_y][cur_x+1]
        cur_x += 1
    while cur_y - 1 >= machine_y:
        grid[cur_y][cur_x] = grid[cur_y - 1][cur_x]
        cur_y -= 1
    while cur_x - 1 >= 0:
        grid[cur_y][cur_x] = grid[cur_y][cur_x-1] if cur_x-1 != machine_x else 0
        cur_x -= 1

def grid_iter(H,W):
    for h_i in range(H):
        for w_i in range(W):
            yield h_i, w_i

def spread():
    global grid
    next_dusts = [[0] * W for _ in range(H)]
    # for h_i in range(H):
    #     for w_i in range(W):
    for h_i, w_i in grid_iter(H, W):
        cur_dust_score = grid[h_i][w_i]
        if cur_dust_score <= 0: continue
        next_dust_score = math.floor(cur_dust_score / 5)
        for n_x, n_y in [(w_i + dx[i], h_i + dy[i]) for i in range(4)]:
            if not (0 <= n_x < W and 0 <= n_y < H): continue
            if grid[n_y][n_x] == -1: continue
            next_dusts[n_y][n_x] += next_dust_score
            next_dusts[h_i][w_i] -= next_dust_score
    # print(*grid, sep='\n')
    for h_i, w_i in grid_iter(H, W):
        grid[h_i][w_i] += next_dusts[h_i][w_i]

for i in range(T):
    spread()
    up_machine()
    down_machine()

res = 0
for h_i, w_i in grid_iter(H, W):
    res += grid[h_i][w_i]
print(res+2)
