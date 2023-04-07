from collections import deque

# 입력
N = int(input())
# 빈칸 0 벽 1
grid = [[0] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    row_in = list(map(int, input().split(' ')))
    for j in range(1, N+1):
        grid[i][j] = row_in[j-1]

# 가로 0, 대각 1, 세로 2
pipe_dir = 0
s_x, s_y = 1, 1

res = 0
tail_dxdy = [(1, 0), (1, 1), (0, 1)]

# 한 지점에서 해당 방향으로 놓을 수 있는 지
def check(x,y,d):
    global grid
    if d == 0:
        if not x + 1 <= N: return False
        if grid[y][x+1] == 1: return False
    elif d == 1:
        if not(x + 1 <= N) or not (y + 1 <= N): return False
        if grid[y][x+1] == 1 or grid[y+1][x+1] == 1 or grid[y+1][x] == 1:
            return False
    elif d == 2:
        if not y + 1 <= N: return False
        if grid[y+1][x] == 1: return False
    return True

def dfs(x, y, d):
    global tail_dxdy, N, res
    tail_x, tail_y = x + tail_dxdy[d][0], y + tail_dxdy[d][1]
    if tail_x == N and tail_y == N:
        res += 1
        return

    # 현재 위치와 방향에 따라 다음 위치 dfs 호출
    if d == 0:
        if check(tail_x, tail_y, 0):
            ans = check(tail_x, tail_y, 0)
            dfs(tail_x, tail_y, 0)
        if check(tail_x, tail_y, 1):
            ans = check(tail_x, tail_y, 1)
            dfs(tail_x, tail_y, 1)
    elif d == 1:
        if check(tail_x, tail_y, 0):
            ans = check(tail_x, tail_y, 0)
            dfs(tail_x, tail_y, 0)
        if check(tail_x, tail_y, 1):
            ans = check(tail_x, tail_y, 1)
            dfs(tail_x, tail_y, 1)
        if check(tail_x, tail_y, 2):
            ans = check(tail_x, tail_y, 2)
            dfs(tail_x, tail_y, 2)
    elif d == 2:
        if check(tail_x, tail_y, 1):
            ans = check(tail_x, tail_y, 1)
            dfs(tail_x, tail_y, 1)
        if check(tail_x, tail_y, 2):
            ans = check(tail_x, tail_y, 2)
            dfs(tail_x, tail_y, 2)


if grid[N][N] == 1:
    print(0)
else:
    dfs(1, 1, 0)
    print(res)