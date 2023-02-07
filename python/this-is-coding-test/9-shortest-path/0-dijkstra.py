# 다익스트라
import heapq

N, E = map(int, input().split())
S = int(input())
INF = int(1e9)

graph = [[] for i in range(N+1)]
distance = [INF] * (N+1)
distance[S] = 0
pq = []

for i in range(E):
    start, end, dist = map(int, input().split(' '))
    graph[start].append((dist, end))

for dist, end in graph[S]:
    heapq.heappush(pq, (dist, end))
    distance[end] = dist

print(graph)

while pq:
    cur_dist, cur_node = heapq.heappop(pq)
    for next_dist, next_node in graph[cur_node]:
        sum_dist = cur_dist + next_dist
        if sum_dist < distance[next_node]:
            distance[next_node] = sum_dist
            heapq.heappush(pq, (sum_dist, next_node))

print(distance)
