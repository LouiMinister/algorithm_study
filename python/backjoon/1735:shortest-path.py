# 최단 경로
import heapq

INF = 312123 * 10 * 21234
V, E = map(int, input().split(' '))
r_node = int(input())
G = {v: [] for v in range(V+1)}

for _ in range(E):
    s_node, e_node, cost = map(int, input().split())
    G[s_node].append((e_node, cost))

pq = []
distance = [INF] * (V + 1)
distance[r_node] = 0

for nxt_node, cost in G[r_node]:
    heapq.heappush(pq, (cost, nxt_node))
    distance[nxt_node] = min(distance[nxt_node], cost)

while pq:
    cur_cost, cur_node = heapq.heappop(pq)
    for nxt_node, nxt_cost in G[cur_node]:
        sum_cost = cur_cost + nxt_cost
        if sum_cost < distance[nxt_node]:
            distance[nxt_node] = sum_cost
            heapq.heappush(pq, (sum_cost, nxt_node))

for d in distance[1:]:
    if d == INF:
        print('INF')
    else:
        print(d)
