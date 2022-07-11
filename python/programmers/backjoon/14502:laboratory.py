import sys
# import time
from collections import deque
from itertools import combinations

# global
N, M = list(map(int, sys.stdin.readline().split()))  # 세로 가로
area = [[0] * (M + 1) for _ in range(N + 1)]
virus = []
wallCnt = 0
candi = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
result = 0


def bfs():
    vis = [[False] * (M + 1) for _ in range(N + 1)]
    virusSize = 0
    q = deque()
    for x, y in virus:
        q.appendleft((x, y))
        vis[y][x] = True
        virusSize += 1
    while len(q) != 0:
        curX, curY = q.pop()
        for i in range(4):
            nx, ny = curX + dx[i], curY + dy[i]
            if not (1 <= nx <= M and 1 <= ny <= N): continue  # 범위초과
            if vis[ny][nx]: continue  # 방문시
            if area[ny][nx] == 1: continue  # 벽
            vis[ny][nx] = True
            q.appendleft((nx, ny))
            virusSize += 1
    return virusSize


# main
for row in range(1, N + 1):
    for col, val in enumerate(list(map(int, sys.stdin.readline().split()))):
        if val == 2:
            virus.append((col + 1, row))
        if val == 1:
            wallCnt += 1
        area[row][col + 1] = val
# start = time.time()
for i in range(1, N + 1):
    for j in range(1, M + 1):
        if area[i][j] == 0:
            candi.append((j, i))
candi = list(combinations(candi, 3))

for walls in candi:
    for wall in walls:
        area[wall[1]][wall[0]] = 1
    result = max(result, M * N - bfs() - wallCnt - 3)
    for wall in walls:
        area[wall[1]][wall[0]] = 0

print(result)
# print(time.time() - start)
