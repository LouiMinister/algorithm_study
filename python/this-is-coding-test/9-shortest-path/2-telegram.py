# 전보
import heapq

INF = int(1e9)
N, E, C = map(int, input().split(' '))
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)
pq = []

for _ in range(E):
    print(1)
    start, end, cost = map(int, input().split(' '))
    graph[start].append((cost, end))

for cost, end in graph[C]:
    distance[end] = cost
    heapq.heappush(pq, (cost, end))

while pq:
    cur_cost, cur_node = heapq.heappop(pq)
    for next_cost, next_node in graph[cur_node]:
        sum_cost = cur_cost+next_cost
        if sum_cost < distance[next_node]:
            distance[next_node] = sum_cost
            heapq.heappush(pq, (sum_cost, next_node))

filtered = list(filter(lambda e: e != INF, distance))
# print(filtered)
print(len(filtered), max(filtered))

