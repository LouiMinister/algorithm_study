# 경쟁적 전염
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
N, V = map(int, input().split(' '))
field = [None] * N
q = []
for i in range(N):
    row_input = list(map(int, input().split(' ')))
    field[i] = row_input
    for j in range(N):
        if row_input[j] > 0:
            q.append((row_input[j], i, j, 0))
T, Y, X = map(int, input().split(' '))
q.sort()
q = deque(q)
while q:
    cur_virus, cur_y, cur_x, cur_time = q.popleft()
    if cur_time == T: break
    for d in range(4):
        next_x, next_y = cur_x + dx[d], cur_y + dy[d]
        if not (0 <= next_x < N and 0 <= next_y < N): continue
        if field[next_y][next_x] == 0:
            field[next_y][next_x] = cur_virus
            q.append((cur_virus, next_y, next_x, cur_time + 1))

print(field[Y-1][X-1])
# print(field)
# print(q)


# 3 3
# 1 0 2
# 0 0 0
# 3 0 0
# 2 3 2