import sys
sys.setrecursionlimit(10**5)
N = int(input())
dis_set = [i for i in range(N+1)]

def upward(x, updated):
  if dis_set[x] == x: return x
  
  updated.append(x)
  return upward(dis_set[x], updated)

def find(x):
  updated = []
  root = upward(x, updated)
  for u in updated:
    dis_set[u] = root
  return root
    
def union(x, y):
  xRoot = find(x)
  yRoot = find(y)
  if xRoot == yRoot: return
  
  dis_set[xRoot] = yRoot

for _ in range(N-2):
  nodes = list(map(int, input().split()))
  union(nodes[0], nodes[1])
    
sep_node = set()
for node in range(1,N+1):
  root = find(node)
  if root not in sep_node:
    sep_node.add(root)

print(" ".join(map(str, list(sep_node))))
