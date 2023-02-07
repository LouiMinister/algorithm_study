N = int(input())
E = int(input())
INF = int(1e9)
graph = [[INF]*(N+1) for _ in range(N+1)]

for i in range(N+1):
    graph[i][i] = 0

for i in range(E):
    start, end, cost = map(int, input().split(' '))
    graph[start][end] = cost

print(graph)

for mid in range(1, N+1):
    for start in range(1, N+1):
        for end in range(1, N+1):
            graph[start][end] = min(graph[start][mid] + graph[mid][end], graph[start][end])

print(graph)