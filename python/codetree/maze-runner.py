# 메이즈 러너

# 오답 노트

# 회전은 하나 하나씩 옮겨 담지 말고 전체를 복사한 담에 회전 후 다시 붙혀넣기를 해야 한다.
# 왜냐하면, 순회 중에 회전을 이미 마친 cell을 방문하는 경우가 생기기 때문이다.

# 최댓 값, 최솟 값, 최적 값 등을 구해야 할 때 중간 산출값의 최대, 최소, 최적 값을 수정 해서 그게 최적값이라고 생각하지 말자.
# 이번 문제에서는 사각형 범위가 음수로 넘어가는 경우 후처리를 해줬는데, 이 후처리 한 결과를 가지고 최대, 최소, 최적값을 구했어야 했다.
# 후처리 코드를 중간에 삽입했기 때문에 별 신경을 못썼다.
# sort, 대소 비교 등의 결과는 항상 sort한 ary[0] 값이 되어야 한다.
# ary[0] + 후처리 -> 가 결과가 되도록 하면 안된다!!!


import copy

dirs = [[0, -1], [0, 1], [-1, 0], [1, 0]]

MAZE_SIZE, PLAYER_CNT, TIME_MAX = map(int, input().split(" "))
maze = [[-1 for _ in range(MAZE_SIZE + 1)]]
for _ in range(MAZE_SIZE):
  maze.append([-1, *map(int, input().split(" "))])
  
players = [None]
playerWalked = 0
playerExited = [False for _ in range(PLAYER_CNT + 1)]
for _ in range(PLAYER_CNT):
  mis = list(map(int, input().split(" ")))
  players.append([mis[1], mis[0]])
  
mis = list(map(int, input().split(" ")))
wayOut = [mis[1], mis[0]]
  
# 최단 거리 좌표 반환
def distance(x1, y1, x2, y2):
  return abs(x1 - x2) + abs(y1 - y2)

# 이동
# 두 위치의 최단 거리 = (x1 - x2) + (y1 - y2)
# 모든 참가잔느 동시에 움직임
# 상하좌우로 움직임
# 벽이 없는곳으로 이동 가능
# 움직인 칸은 머물러 있던 칸보다 출구까지의 최단거리가 가까워야 함
# 움직일 수 있는 칸이 2개 이상이라면, 상하 움직임 우선
# 움직일 수 없으면 움직이지 않음
# 한칸에 두명 이상 참가자 있을 수 있음
# 도달하면 즉시 탈출
def move():
  global playerWalked, players, playerExited
  for pi in range(1, PLAYER_CNT + 1):
    if playerExited[pi]: continue
    
    curPos = players[pi]
    curDistance = distance(*curPos, *wayOut)
    nextPos = None
    for dir in dirs:
      nx, ny = curPos[0] + dir[0], curPos[1] + dir[1]
      if nx <= 0 or ny <= 0 or nx > MAZE_SIZE or ny > MAZE_SIZE: continue
      if maze[ny][nx] > 0: continue
      nDistance = distance(nx, ny, *wayOut)
      if nDistance < curDistance:
        nextPos = [nx, ny]
        break
    # print("NEXTPOS", pi, nextPos)
    if nextPos == None: continue
    if nextPos == wayOut: playerExited[pi] = True
    playerWalked += 1
    players[pi] = nextPos


# 가장 작은 정사각형 좌표

# max((출구x - 유저x), (출구y - 유저y)) 가 가장 작은 유저 -> 정사각형의 크기 도출 가능
# 이거 배열 만들어서 소트해가지고, 후보 유저들 추리기

# 두 점 중 y축이 더 큰 것이 사각형의 바닥 좌표 결정
# 두 점 중 x축이 더 큰 것이 사각형의 우측 좌표 결정

# 사각형 중 제일 작은거 고르기

# 한 명 이상의 참가자와 출구를 포함한 가장 작은 정사각형
#   2개 이상이면 좌상단 r 좌표가 작은것이 우선. 그래도 같으면 c 좌표가 작은 것이 우선

def minRect():
  candi = []
  for pi in range(1, PLAYER_CNT + 1):
    if playerExited[pi]: continue
    playerPos = players[pi]
    cost = max(abs(wayOut[0] - playerPos[0]), abs(wayOut[1] - playerPos[1]))
    candi.append([cost, playerPos[0], playerPos[1]])
    
  candi.sort()
  # print("CANDI", candi)
  minSize = candi[0][0]
  candi = [c for c in candi if c[0] == minSize]
  # print("CANDI", candi, minSize)
  
  rectCandi = []
  for c in candi:
    playerPos = [c[1], c[2]]
    startPos = [max(playerPos[0], wayOut[0]) - minSize, max(playerPos[1], wayOut[1]) - minSize]
    padPos = [max(0, 1 - startPos[0]), max(0, 1 - startPos[1])]
    rectCandi.append([startPos[1] + padPos[1], startPos[0] + padPos[0]])
  rectCandi.sort()
  # print("RECT CANDI", rectCandi)
  
  endDot = rectCandi[0]
  rect = [endDot[1], endDot[0], endDot[1] + minSize, endDot[0] + minSize]
  # print("RECT BEF", rect)
  # padPos = [max(0, 1 - rect[0]), max(0, 1 - rect[1])]
  # rect = [rect[0] + padPos[0], rect[1] + padPos[1], rect[2] + padPos[0], rect[3] + padPos[1]]
  # 0보다 작거나 같을 때 처리
  
  # print("RECT", rect)
  return rect


def spinCoord(x, y, axisX, axisY, W):
  nx, ny = x - axisX, y - axisY
  nx, ny = [W - ny, nx]
  nx, ny = [nx + axisX, ny + axisY]
  return [nx, ny]
  
# 회전
# 모든 참가자 이동 후 회전
# 선택한 정사각형은 시계방향으로 90도 회전. 회전된 벽은 내구도 1씩 깎임

# 벽
#   1 이상 9 이하 내구도
#   회전 시 내구도 1식 깎임
#   0되면 빈 칸
def rotate():
  global wayOut, maze, players
  rect = minRect()
  startDot = [rect[0], rect[1]]
  endDot = [rect[2], rect[3]]
  W = endDot[0] - startDot[0]
  nMaze = copy.deepcopy(maze)
  nPlayers = copy.deepcopy(players)
  nWayOut = copy.deepcopy(wayOut)
  
  for yi in range(startDot[1], endDot[1] + 1):
    for xi in range(startDot[0], endDot[0] + 1):
      spinedPos = spinCoord(xi, yi, *startDot, W)
      nMaze[spinedPos[1]][spinedPos[0]] = max(0, maze[yi][xi]-1)
      
      for pi in range(1, PLAYER_CNT + 1):
        if playerExited[pi]: continue
        if players[pi] == [xi, yi]:
          # print("MATCHED", players[pi])
          nPlayers[pi] = copy.deepcopy(spinedPos)
      
      if wayOut == [xi, yi]:
        nWayOut = copy.deepcopy(spinedPos)
  
  maze = nMaze
  players = nPlayers
  wayOut = nWayOut
        
def allExited():
  for i in range(1, PLAYER_CNT + 1):
    if not playerExited[i]:
      return False
  return True
  
def mazePosIter():
  for yi in range(1, MAZE_SIZE+1):
    for xi in range(1, MAZE_SIZE+1):
      yield([xi, yi])

def printMaze():
  nMaze = copy.deepcopy(maze)
  for i in range(1, PLAYER_CNT + 1):
    if playerExited[i]: continue
    nMaze[players[i][1]][players[i][0]] = "!"
    
  nMaze[wayOut[1]][wayOut[0]] = "$"
  
  for yi in range(1, MAZE_SIZE+1):
    print(nMaze[yi][1:])

  print("")
    
# print("FIRST")
# print("PLAYERS", players)
  
# K 초 동안 반복
# K초 전에 모두 탈출 -> 게임 끝
# 모든 참가자들의 이동거리 합 + 출구 좌표 출력
for curTime in range(1, TIME_MAX + 1):
  # 유저 이동
  move()
  # print("")
  # print("MOVE PLAYERS", players)
  # print("PLAYER EXITED", playerExited)
  # 맵 회전
  # printMaze()
  # print("ROTATE")
  # print("MINRECT", minRect())
  if allExited(): break
  rotate()
  # printMaze()
  # print("MOVE PLAYERS", players)
  # print("EXIT", wayOut)
  
print(playerWalked)
print(wayOut[1], wayOut[0])


# print(minRect())
# rotate()
# printMaze()
