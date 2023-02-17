# 특정 거리의 도시 찾기
import heapq

N, E, D, S = map(int, input().split(' '))

graph = [[] for _ in range(N+1)]
distance = [10000001 for _ in range(N+1)]
distance[S] = 0

for i in range(E):
    node_s, node_e = map(int, input().split(' '))
    graph[node_s].append(node_e)

pq = []
for node in graph[S]:
    heapq.heappush(pq, (1, node))
    distance[node] = 1

while pq:
    cur_distance, cur_node = heapq.heappop(pq)
    for nxt_node in graph[cur_node]:
        sum_distance = cur_distance + 1
        if sum_distance < distance[nxt_node]:
            distance[nxt_node] = sum_distance
            heapq.heappush(pq, (sum_distance, nxt_node))
res = []
for i in range(N+1):
    if distance[i] == D:
        res.append(i)
if res:
    print(*res, sep='\n')
else:
    print(-1)
