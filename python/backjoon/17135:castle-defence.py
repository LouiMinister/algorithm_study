# 캐슬 디펜스

from itertools import combinations
from collections import deque
import copy
#
# 5 5 1
# 1 1 1 1 1
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 1 1 1 1 1
def kill_round(grid, D):
    result = 0
    dx = [-1, 0, 1]
    dy = [0, -1, 0]
    H = len(grid) - 1
    W = len(grid[0])

    # 궁수 순회
    target = set()
    for archer_x in range(len(grid[0])):
        if grid[H][archer_x] != 2: continue

        # bfs 순회
        vis = [[False] * W for _ in range(H + 1)]
        trace = deque()
        trace.append((archer_x, H, 0))
        while trace:
            cur_x, cur_y, cur_dist = trace.popleft()
            # print(grid)
            if cur_dist > D: break
            vis[cur_y][cur_x] = True
            if grid[cur_y][cur_x] == 1: # 적이 있는 경우
                target.add((cur_x, cur_y)) # 중복 타겟 고려
                break
            # 주변 순회
            for i in range(3):
                next_x, next_y, next_dist = cur_x + dx[i], cur_y + dy[i], cur_dist + 1
                if not (0 <= next_x < W and 0 <= next_y < H): continue
                if vis[next_y][next_x]: continue
                trace.append((next_x, next_y, next_dist))
    # 죽인 수 반환
    for target_x, target_y in target:
        grid[target_y][target_x] = 0
        result += 1

    return result

def move_round(grid):
    archer_line = len(grid) - 1
    W = len(grid[0])
    grid.pop(archer_line-1)
    return [[0] * W] + grid

def is_all_dead(grid):
    for row in grid:
        for cell in row:
            if cell == 1: return False
    return True

result = 0
H, W, D = map(int, input().split(' '))
grid = []
for i in range(H):
    grid.append(list(map(int, input().split(' '))))
grid.append(None) # 궁수 자리
grid_origin = copy.deepcopy(grid)

candi = [i for i in range(W)]
positions = combinations(candi, 3)
for position in positions: # 궁수 위치
    grid = grid = copy.deepcopy(grid_origin)
    grid[H] = [0] * W
    for p in position: # 궁수 배치
        grid[H][p] = 2
    killed = 0
    for _ in range(H):
        # 궁수 사격
        # print(grid)
        killed += kill_round(grid, D)
        # 전진
        grid = move_round(grid)
        if is_all_dead(grid): break
    result = max(result, killed)
print(result)
