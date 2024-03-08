import sys
from collections import deque

N, K = list(map(int, sys.stdin.readline().split()))
vis_on_step = set()


def bfs(now):
    q = deque()
    q.appendleft((now, 0))
    vis_on_step.add(now)
    while len(q) != 0:
        node, time = q.pop()
        if node == K:
            return time
        if node - 1 not in vis_on_step and 0 <= node - 1 <= 200000:
            q.appendleft((node - 1, time + 1))
            vis_on_step.add(node - 1)
        if node + 1 not in vis_on_step and 0 <= node + 1 <= 200000:
            q.appendleft((node + 1, time + 1))
            vis_on_step.add(node + 1)
        if node * 2 not in vis_on_step and 0 <= node * 2 <= 200000:
            q.appendleft((node * 2, time + 1))
            vis_on_step.add(node * 2)


print(bfs(N))
