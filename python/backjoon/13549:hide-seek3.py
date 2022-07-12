import sys
from collections import deque

N, K = list(map(int, sys.stdin.readline().split()))
vis = set()


def bfs(now):
    q = deque()
    q.appendleft((now, 0))
    vis.add(now)
    while len(q) != 0:
        node, time = q.pop()
        if node == K:
            return time
        if node * 2 not in vis and 0 <= node * 2 <= 200000:
            q.appendleft((node * 2, time))
            vis.add(node * 2)
        if node - 1 not in vis and 0 <= node - 1 <= 200000:
            q.appendleft((node - 1, time + 1))
            vis.add(node - 1)
        if node + 1 not in vis and 0 <= node + 1 <= 200000:
            q.appendleft((node + 1, time + 1))
            vis.add(node + 1)

print(bfs(N))
