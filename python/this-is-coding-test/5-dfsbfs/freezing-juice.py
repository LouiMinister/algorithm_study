# 음료수 얼려먹기

res = 0
graph = []
N, M = map(int, input().split(' '))

for i in range(N):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if not (0 <= x < M and 0 <= y < N): return
    global graph
    if graph[y][x] == 1: return
    graph[y][x] = 1
    dfs(x + 1, y)
    dfs(x, y + 1)
    dfs(x - 1, y)
    dfs(x, y - 1)


for y in range(N):
    for x in range(M):
        if graph[y][x] == 0:
            res += 1
            dfs(x, y)
print(res)
