# m명의 사람 - m 번 사람은 m분에 출발
# 출발 시간 전에는 겪자 밖에 있음
# n*n 크기의 격자



# 지나갈 수 있는 칸 여부 2차원 배열

from collections import deque
import copy

BOARD_SIZE, PLAYER_CNT = map(int, input().split(" "))
board = [[None for _ in range(BOARD_SIZE + 1)]]
for _ in range(BOARD_SIZE):
  board.append([None, *map(int, input().split(" "))])
destinations = [None]
for _ in range(PLAYER_CNT):
  mis = list(map(int, input().strip().split(" ")))
  # print("MIS", mis)
  destinations.append([mis[1], mis[0]])

players = [None for _ in range(PLAYER_CNT + 1)]
arrivedAt = [None for _ in range(PLAYER_CNT + 1)]
    
    
def printBoard():
  for y in range(1, BOARD_SIZE + 1):
    print(board[y][1:])
  print("")
  
def isOutOfBoard(x, y):
  return x < 1 or y < 1 or x > BOARD_SIZE or y > BOARD_SIZE
    
# 현재 편의점으로 갈 수 있는 최단거리 베이스캠프
# 행동
# 1. 격자에 있는 사람들 - 가고 싶은 편의점 방향으로 1칸 이동 (최단거리로)
#     최단거리 = 이동 가능한 칸으로만 이동하여 거쳐야 하는 칸 수 최소가 되는 거리
#     상 좌 우 하 우선순위
def getShortestPath(sx, sy, ex, ey):
  vis = [[False for _ in range(BOARD_SIZE + 1)] for _ in range(BOARD_SIZE + 1)]
  dq = deque()
  vis[sy][sx] = True
  dq.append([[sx, sy]])
  
  while dq:
    path = dq.popleft()
    x, y = path[-1]
    for dx, dy in [[0, -1], [-1, 0], [1, 0], [0, 1]]:
      nx, ny = x + dx, y + dy
      # print(nx, ny)
      if isOutOfBoard(nx, ny): continue
      if board[ny][nx] == -1: continue
      if vis[ny][nx]: continue
      
      vis[ny][nx] = True
      nPath = copy.deepcopy(path)
      nPath.append([nx, ny])
      # print("PATH", nPath)
      if (nx, ny) == (ex, ey): return nPath
      dq.append(nPath)
  
  return None
  

# 3. 현재 시간 t, 사람 m -> t <= m 이면 t번 사람은 가고 싶은 편의점과 가장 가까이 있는 베이스캠프에 들어감
#     1과 같이 최단거리 = 가까운 곳
#     (거리, y, x) 거리가 작은곳, 행이 작은 곳, 열이 작은 곳
#     이 때 부터 해당 베이스 캠프 있는 칸 지나갈 수 없음
#         (사람이 나가도 절대 못지나감)
def getNearestBase(sx, sy):
  vis = [[False for _ in range(BOARD_SIZE + 1)] for _ in range(BOARD_SIZE + 1)]
  dq = deque()
  vis[sy][sx] = True
  dq.append([sx, sy, 0])
  
  baseCandi = []
  shortestDist = BOARD_SIZE ** 3
  
  # print("")
  # print("NEAREST BASE",[sx, sy])
  # printBoard()
  
  while dq:
    # print("dq", dq)
    cx, cy, cd = dq.popleft()
    for dx, dy in [[0, -1], [-1, 0], [1, 0], [0, 1]]:
      nx, ny = cx + dx, cy + dy
      nd = cd + 1
      # print(nx, ny)
      if isOutOfBoard(nx, ny): continue
      if board[ny][nx] == -1: continue
      if vis[ny][nx]: continue
      
      vis[ny][nx] = True
      if board[ny][nx] == 1:
        if nd <= shortestDist:
          shortestDist = nd
          baseCandi.append([ny, nx])
        else:
          break
      else:
        dq.append([nx, ny, nd])
    
  baseCandi.sort()
  # print(baseCandi)
  nearestBase = [baseCandi[0][1], baseCandi[0][0]]
  return nearestBase
  
def isAllArrived():
  for i in range(1, PLAYER_CNT+1):
    if arrivedAt[i] == None:
      return False
  return True


# printBoard()
# print(destinations)


# 행동
# 1. 격자에 있는 사람들 - 가고 싶은 편의점 방향으로 1칸 이동 (최단거리로)
#     최단거리 = 이동 가능한 칸으로만 이동하여 거쳐야 하는 칸 수 최소가 되는 거리
#     상 좌 우 하 우선순위

# 2. 편의점 도착시 편의점에 멈춤. 이때부터 다른 사람들은 해당 편의점 칸 지나갈 수 없음
#     (이동 후에 적용되는거임)
    
# 3. 현재 시간 t, 사람 m -> t <= m 이면 t번 사람은 가고 싶은 편의점과 가장 가까이 있는 베이스캠프에 들어감
#     1과 같이 최단거리 = 가까운 곳
#     (거리, y, x) 거리가 작은곳, 행이 작은 곳, 열이 작은 곳
#     이 때 부터 해당 베이스 캠프 있는 칸 지나갈 수 없음
#         (사람이 나가도 절대 못지나감)

curSec = 0
while True:
  curSec += 1
  
  # 1
  for pi in range(1, PLAYER_CNT + 1):
    playerPos = players[pi]
    if arrivedAt[pi] != None: continue
    if playerPos == None: continue
    playerDestination = destinations[pi]
    path = getShortestPath(*playerPos, *playerDestination)
    nPos = path[1] # CHK: path가 항상 1보다 커야 함
    players[pi] = nPos
  
  # 2
  for pi in range(1, PLAYER_CNT + 1):
    playerPos = players[pi]
    if arrivedAt[pi] != None: continue
    if playerPos == None: continue
    
    if playerPos == destinations[pi]:
      arrivedAt[pi] = curSec
      players[pi] = None
      board[playerPos[1]][playerPos[0]] = -1

  # 3
  # 현재 베이스캠프 이동할 사람
  if curSec <= PLAYER_CNT:
    playerDestination = destinations[curSec]
    # 목적지 편의점과 가장 가까운 베이스캠프 찾기
    nearestBasePos = getNearestBase(*playerDestination)
    # 그 사람 위치를 그 베이스캠프로 이동시키고, 베이스 캠프 칸 -1로 만들기
    players[curSec] = nearestBasePos
    board[nearestBasePos[1]][nearestBasePos[0]] = -1
    
  if isAllArrived(): break

print(max(arrivedAt[1:]))
# print(getShortestPath(1, 4, 3, 2))
# print(getNearestBase(5,4))
