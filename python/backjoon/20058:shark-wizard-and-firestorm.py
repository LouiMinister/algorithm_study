# 마법사 상어와 파이어스톰

# 2^N x 2^
# r행 c열 A[r][c] (0이면 노얼음)
# L -> 2^L 2^L 격자, 90도 회전
# 얼음 3개 이상 인접해있지 않은 칸 -= 1
#
# 결과
# 남아있는 얼음의 합
# 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수

from collections import deque

## 입력
N, Q = map(int, input().split(' '))
W = 2**N
grid = [list(map(int, input().split(' '))) for _ in range(W)]
commands = list(map(int, input().split(' ')))

## 함수
# 왼쪽 끝 좌표 x,y 와 격자 크기 w를 받아 회전시키는 함수
def rotate(x,y,w):
    global grid
    tmp = [[0] * w for _ in range(w)]
    for i in range(w):
        for j in range(w):
            tmp[j][w-i-1] = grid[i + y][j + x]
    for i in range(w):
        for j in range(w):
            grid[i+y][j+x] = tmp[i][j]

# 얼음 3개 이상 인접해있지 않으면 녹이는 함수
def melt():
    global grid, W
    will_melt = []
    for i in range(W):
        for j in range(W):
            if grid[i][j] == 0: continue
            cnt = 0
            for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
                if not (0 <= i+dy < W and 0 <= j+dx < W): continue
                if grid[i+dy][j+dx] > 0: cnt += 1
            if cnt < 3: will_melt.append((j, i))
    for x, y in will_melt:
        grid[y][x] -= 1

# 남아있는 얼음의 합을 구하는 함수
def cnt_ice():
    global grid, W
    cnt = 0
    for i in range(W):
        for j in range(W):
            cnt += grid[i][j]
    return cnt

# 얼음 중 가장 큰 덩어리가 차지하는 칸 의 개수 구하는 함수
def bfs(x, y, vis):
    global grid, W
    if vis[y][x]: return 0
    if grid[y][x] == 0: return 0
    q = deque()
    q.append((x,y))
    cnt = 0
    while q:
        cur_x, cur_y = q.pop()
        if grid[cur_y][cur_x] == 0: continue
        if vis[cur_y][cur_x]: continue
        vis[cur_y][cur_x] = True
        cnt += 1
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            if not (0 <= cur_x + dx <W and 0<= cur_y + dy <W): continue
            if vis[cur_y+dy][cur_x+dx]: continue
            q.append((cur_x+dx, cur_y+dy))
    return cnt

def biggest_ice_cnt():
    global grid, W
    max_cnt = 0
    vis = [[False] * W for _ in range(W)]
    for i in range(W):
        for j in range(W):
            max_cnt = max(max_cnt, bfs(j, i, vis))
    return max_cnt

def grid_corner_pos(L):
    global W
    cell_w = 2**L
    for i in range(0, int(W / cell_w)):
        for j in range(0, int(W / cell_w)):
            yield j * cell_w, i * cell_w

# 실행
for cmd in commands:
    for cell_x, cell_y in grid_corner_pos(cmd):
        rotate(cell_x, cell_y, 2**cmd)
    melt()
print(cnt_ice())
print(biggest_ice_cnt())

# 3 1
# 1 2 3 4 5 6 7 8
# 1 2 3 4 5 6 7 8
# 1 2 3 4 5 6 7 8
# 1 2 3 4 5 6 7 8
# 1 2 3 4 5 6 7 8
# 1 2 3 4 5 6 7 8
# 1 2 3 4 5 6 7 8
# 1 2 3 4 5 6 7 8
# 3
