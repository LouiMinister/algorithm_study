# 가장 먼 노드

import heapq


def solution(n, edge):
    MAX = 999999999
    # 그래프 만들기
    graph = [[] for i in range(n + 1)]
    for n1, n2 in edge:
        graph[n1].append(n2)
        graph[n2].append(n1)

    # 다익스트라
    # 결과값 배열 만들기
    dist = [MAX] * (n + 1)
    pq = []
    heapq.heappush(pq, (0, 1))
    dist[1] = 0
    # pq 에  거리, 첫 노드 담기

    # pq에서 뽑아가면서 순회
    while pq:
        cur_dist, cur_node = heapq.heappop(pq)
        if cur_dist < dist[cur_node]: continue

        for next_node in graph[cur_node]:
            next_dist = cur_dist + 1
            if next_dist < dist[next_node]:
                dist[next_node] = next_dist
                heapq.heappush(pq, (next_dist, next_node))

    max_dist = 0
    res = 0
    for d in dist:
        if d != MAX:
            max_dist = max(max_dist, d)
    # print(max_dist)
    for idx, d in enumerate(dist):
        if d == max_dist:
            res += 1
    return res

    # 뽑은거에서 다음으로 이어지는거 순회하면서 결과값 배열 비교 후 업데이트