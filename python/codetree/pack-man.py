# 팩맨

# m개의 몬스터, 1개의 팩맨
# 몬스터 이동 - 상하좌우, 대각선 방향 중 하나


import copy
from itertools import product

DIRS = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
BOARD_SIZE = 4
MOB_CNT, TURN_CNT = map(int, input().split(" "))
mis = list(map(int, input().split(" ")))
pac = [mis[1], mis[0]]
mobBoard = [[[] for _ in range(BOARD_SIZE + 1)] for _ in range(BOARD_SIZE + 1)]
for _ in range(MOB_CNT):
  mis = list(map(int, input().split(" ")))
  mobBoard[mis[0]][mis[1]].append(mis[2]-1)
  
# 각 cell은 [dir...]
eggBoard = [[[] for _ in range(BOARD_SIZE + 1)] for _ in range(BOARD_SIZE + 1)]
# 각 cell은 [남은턴]
# CHK: dead body update는 max로
deadBoard = [[0 for _ in range(BOARD_SIZE + 1)] for _ in range(BOARD_SIZE + 1)]


# 함수
def printMobBoard():
  print("PRINT MobBoard")
  for y in range(1, BOARD_SIZE + 1):
    print(mobBoard[y][1:])
    
def printEggBoard():
  print("PRINT EggBoard")
  for y in range(1, BOARD_SIZE + 1):
    print(eggBoard[y][1:])
    
def printDeadBoard():
  print("PRINT DeadBoard")
  for y in range(1, BOARD_SIZE + 1):
    print(deadBoard[y][1:])

def boardIter():
  for y in range(1, BOARD_SIZE + 1):
    for x in range(1, BOARD_SIZE + 1):
      yield [x, y]
      
def isOutOfBoard(x, y):
  return x < 1 or y < 1 or x > BOARD_SIZE or y > BOARD_SIZE 


# 한 턴
# 1. 몬스터 복제 시도
# 현재 위치에서 몬스터 복제
# 자신이 가진 방향과 같은 방향을 가짐
# 아직은 부화하지 않은 상태로 움직이지 못함
def makeEgg():
  for x, y in boardIter():
    mobs = mobBoard[y][x]
    for mobDir in mobs:
      eggBoard[y][x].append(mobDir)

# 2. 몬스터 이동
# 자신이 가진 방향대로 한 칸 이동
# 움직이려는 칸에 몬스터 시체 or 팩맨 or 격자 벗어나는 방향 -> 반시계 45도 회전 후 갈 수 있는지 체크
#   가능할 때 까지 반시계 방향을 회전.
#   8방향 다 돌았는데 불가능하면 움직이지 않음
# (몬스터는 겹칠 수 있음)
def moveMobs():
  global mobBoard
  nMobBoard = [[[] for _ in range(BOARD_SIZE + 1)] for _ in range(BOARD_SIZE + 1)]
  for x, y in boardIter():
    mobs = mobBoard[y][x]
    for mobDir in mobs:
      moveToX, moveToY = x, y 
      for di in range(8):
        curDir = DIRS[(mobDir + di) % 8]
        nx, ny = x + curDir[0], y + curDir[1]
        if isOutOfBoard(nx, ny): continue
        if deadBoard[ny][nx] > 0: continue
        # print("NXNY, PAC, ", nx, ny, pac)
        if nx == pac[0] and ny == pac[1]: continue
        moveToX, moveToY = nx, ny
        break
      if (moveToX == x and moveToY == y):
        nMobBoard[moveToY][moveToX].append((mobDir) % 8)
      else:
        nMobBoard[moveToY][moveToX].append((mobDir + di) % 8) #CHK: di 제대로 맞는지, 특히 한바퀴 돌았을 때
  mobBoard = nMobBoard
  
# 3. 팩맨 이동
# 총 3칸 이동 가능
# 이동마다 상하좌우의 선택지
# 몬스터를 가장 많이 먹을 수 있는 방향으로 이동 (64가지 경우의 수)
#   같다면 상-좌-하-우 우선순위
#   이동중 격자 밖을 나갈 수는 없음
# 이동하는 칸에 몬스터를 모두 먹어치운 후, 그 자리에 몬스터 시체를 남김
# 알은 먹지 않고, 움직이기 전에 함께 있었던 몬스터도 먹지 않음(이동하는 과정의 몬스터만 먹음)

def movePac():
  global mobBoard, deadBoard, pac
  # simulation
  pathCandis = product([[0, -1], [-1, 0], [0, 1], [1, 0]], repeat=3)
  bestEatenMobsCnt = -1
  bestPath = None
  for path in pathCandis:
    isNotValid = False
    vis = set()
    x, y = pac
    eatenMobsCnt = 0
    for pi, dir in enumerate(path):
      x, y = x + dir[0], y + dir[1]
      if isOutOfBoard(x, y): # CHK: 뭔가 사이드 이펙트 조심
        isNotValid = True
        break
      if (x, y) not in vis:
        eatenMobsCnt += len(mobBoard[y][x])
      vis.add((x, y))
      if eatenMobsCnt > bestEatenMobsCnt and pi == 2:
        bestEatenMobsCnt = eatenMobsCnt
        # print("PATH!!", path)
        bestPath = path
    if isNotValid: continue
  
  # print("BEST PATH: ", bestPath)
  # action
  x, y = pac
  for dir in bestPath:
    x, y = x + dir[0], y + dir[1]
    curMobs = mobBoard[y][x]
    if len(curMobs) > 0:
      mobBoard[y][x].clear()
      deadBoard[y][x] = 3
    
  pac = [x, y]
  
# 4. 몬스터 시체 소멸
# 몬스터의 시체는 2턴동안만 유지
def decayDead():
  global deadBoard
  for x, y in boardIter():
    deadBoard[y][x] = max(deadBoard[y][x] - 1, 0)

# 5. 몬스터 복제 완성
# 알 형태의 몬스터 부화. 처음 복제가 된 몬스터 방향을 지닌 채로 깨어남
def hatchEgg():
  global mobBoard, eggBoard
  for x, y in boardIter():
    eggs = eggBoard[y][x]
    for eggDir in eggs:
      mobBoard[y][x].append(eggDir)
    eggBoard[y][x].clear()
  
def countSurvivedMobs():
  res = 0
  for x, y in boardIter():
    res += len(mobBoard[y][x])
  return res

# print("INIT")
# print("PAC", pac)
# printMobBoard()
# printEggBoard()
# printDeadBoard()


for turn in range(1, TURN_CNT+1):
  # print("")
  # print("TURN ", turn)
  # print("MAKE EGG")
  makeEgg()
  # printEggBoard()
  # print("MOVE MOBS")
  moveMobs()
  # printMobBoard()
  # print("BEFORE MOVEPAC")
  # printMobBoard()
  # print("PAC", pac)
  # print("MOVE PAC")
  movePac()
  # printMobBoard()
  # printEggBoard()
  # printDeadBoard()
  
  # print("MOVEPAC END")
  # print("DECAY DEAD")
  decayDead()
  # printDeadBoard()
  # print("HATCH EGG")
  hatchEgg()
  # printEggBoard()
  # printMobBoard()
  
# print("PAC", pac)
# printMobBoard()
# printEggBoard()
# printDeadBoard()

print(countSurvivedMobs())

# printMobBoard()
# printEggBoard()
# makeEgg()
# printEggBoard()

# print("#MOVE MOBS")
# moveMobs()
# printMobBoard()
# print("#MOVE MOBS")
# moveMobs()
# printMobBoard()
# print("#MOVE MOBS")
# moveMobs()
# printMobBoard()

# print("")
# print("#MOVE PACS")
# movePac()
# print(pac)
# printMobBoard()
# printDeadBoard()

# print("#MOVE PACS")
# movePac()
# print(pac)
# printMobBoard()
# printDeadBoard()

# print("#MOVE PACS")
# movePac()
# print(pac)
# printMobBoard()
# printDeadBoard()
