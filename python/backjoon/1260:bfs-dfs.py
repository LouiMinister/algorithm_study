from collections import deque

N, E, S = map(int, input().split(' '))

graph = [[] for _ in range(N+1)]
heap = []
for _ in range(E):
    in1, in2 = map(int, input().split(' '))
    graph[in1].append(in2)
    graph[in2].append(in1)
for i in range(N+1):
    graph[i].sort()

def dfs(start):
    global graph
    res = []
    stack = deque()
    vis = [False] * (N+1)
    stack.append(start)
    while stack:
        cur_node = stack.pop()
        if vis[cur_node]: continue
        vis[cur_node] = True
        res.append(cur_node)
        for next_node in graph[cur_node][::-1]:
            if vis[next_node] is False:
                stack.append(next_node)
    return res

def bfs(start):
    global graph
    res = []
    stack = deque()
    vis = [False] * (N+1)
    stack.append(start)
    while stack:
        cur_node = stack.popleft()
        if vis[cur_node]: continue
        vis[cur_node] = True
        res.append(cur_node)
        for next_node in graph[cur_node]:
            if vis[next_node] is False:
                stack.append(next_node)
    return res

print(*dfs(S))
print(*bfs(S))