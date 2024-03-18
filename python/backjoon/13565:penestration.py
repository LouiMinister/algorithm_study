import sys
from collections import deque
sys.setrecursionlimit(100000)

YMAX, XMAX = map(int, input().split(" "))
field = []
vis = [[False for _ in range(XMAX)] for _ in range(YMAX)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


for _ in range(YMAX):
  field.append(list(map(int, list(input()))))
  
def isOutOfField(x, y):
    return x < 0 or y < 0 or x >= XMAX or y > YMAX

def bfs(x, y):
  
  dq = deque()
  if(y == YMAX - 1): return True
  if(field[y][x] == 1): return False
  dq.append((x, y))
  
  while dq:
    curx, cury = dq.popleft()
    for i in range(4):
      nx = curx + dx[i]
      ny = cury + dy[i]
      
      if isOutOfField(nx, ny): continue
      if field[ny][nx] == 1: continue
      if vis[ny][nx]: continue
      vis[ny][nx] = True
      if(ny == YMAX - 1): return True
      dq.append((nx, ny))

for x in range(XMAX):
  vis[0][x] = True
  if bfs(x, 0): 
    print("YES")
    exit()
    
print("NO")
