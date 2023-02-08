# 미래 도시
INF = int(1e9)
N, E = map(int, input().split(' '))
graph = [[INF] * (N + 1) for _ in range(N + 1)]

for _ in range(E):
    node1, node2 = map(int, input().split(' '))
    graph[node1][node2] = 1
    graph[node2][node1] = 1

for _ in range(N):
    graph[N][N] = 0

L, F = map(int, input().split(' '))


for mid in range(1, N+1):
    for start in range(1, N+1):
        for end in range(1, N+1):
            graph[start][end] = min(graph[start][end], graph[start][mid] + graph[mid][end])

result = graph[1][F] + graph[F][L]

if result >= INF:
    print(-1)
else:
    print(result)

