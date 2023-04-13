import sys
sys.setrecursionlimit(10 ** 5)

N = int(input())
G = dict() # val: (node, cost)

for _ in range(N-1):
    p_node, c_node, edge = map(int, input().split(' '))
    if p_node not in G:
        G[p_node] = []
    G[p_node].append((c_node, edge))

max_res = 0

def dfs(node, cost):
    global res, max_res
    # 끝 점 인 경우
    if node not in G:
        return cost
    # 끝 점이 아닌 경우
    cur_edges = []
    for c_node, c_cost in G[node]:
        c_res = dfs(c_node, c_cost)
        cur_edges.append(c_res)
    cur_edges.sort()
    max_res = max(max_res, sum(cur_edges[-2:]))
    return cur_edges[-1] + cost

dfs(1, 0)
print(max_res)