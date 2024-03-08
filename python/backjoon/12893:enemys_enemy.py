# 이분 그래프 (이분매칭) 개념을 못떠올려서 애먹음

from collections import deque

N, E = map(int, input().split(' '))

nodeColor = [0 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]

for _ in range(E):
  node1, node2 = map(int, input().split(' '))
  graph[node1].append(node2)
  graph[node2].append(node1)
  
def bfs(sNode, color):
  dq = deque()
  dq.append(sNode)
  if nodeColor[sNode] == 0:
    nodeColor[sNode] = color
  while dq:
    curNode = dq.popleft()
    curNodeColor = nodeColor[curNode]
    for nNode in graph[curNode]:
      nNodeColor = nodeColor[nNode]
      if nNodeColor == 0:
        nodeColor[nNode] = curNodeColor * -1
        dq.append(nNode)
      else:
        if nNodeColor != curNodeColor * -1:
          return 0
  return 1

def proc():
  for i in range(1, N+1):
    if bfs(i, 1) == 0:
      return 0
  return 1

print(proc())
