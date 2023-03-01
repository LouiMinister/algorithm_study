# 아이템 줍기

from collections import deque


# 테두리 = 1, 내부 = 2 로. 그리고 2배
def fill(grid, rectangle):
    for x1, y1, x2, y2 in rectangle:
        for i in range(y1 * 2, (y2 * 2) + 1):
            for j in range(x1 * 2, (x2 * 2) + 1):
                if i == y1 * 2 or i == y2 * 2 or j == x1 * 2 or j == x2 * 2:  # 외각
                    if grid[i][j] == 2: continue  # 내부이면 제외
                    grid[i][j] = 1
                else:  # 내부
                    grid[i][j] = 2


# 외각선 + 외각선 = 외각선
# 내부 + 내부 = 내부


def solution(rectangle, characterX, characterY, itemX, itemY):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    grid = [[0] * 110 for _ in range(110)]
    fill(grid, rectangle)

    trace = deque()
    trace.append((characterX * 2, characterY * 2, 0))
    vis = [[False] * 110 for _ in range(110)]

    # bfs 순회. 공간이 1인것만 따라가면 됨. 0, max 도달할 일 없음
    result = -1
    while trace:
        cur_x, cur_y, cur_dist = trace.popleft()
        if cur_x == itemX * 2 and cur_y == itemY * 2:
            result = cur_dist
        # if vis[cur_y][cur_x]: continue
        vis[cur_y][cur_x] = True
        # print(cur_x, cur_y)
        for i in range(4):
            next_x, next_y, next_dist = cur_x + dx[i], cur_y + dy[i], cur_dist + 1
            if vis[next_y][next_x]: continue
            if grid[next_y][next_x] == 1:
                trace.append((next_x, next_y, next_dist))

    return result / 2




