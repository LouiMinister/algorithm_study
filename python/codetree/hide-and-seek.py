# N x N 격자. 술래는 정중앙
# m 명의 도망자

# 상하도망자 - 항상 아래쪽 보고 시작
# 좌우도망자 - 항상 오른쪽 보고 시작

# h개의 나무 (도망자랑 겹칠 수 있음)





  
import math 
import copy

# 초기화
# 
# 0: 상, 1: 우, 2: 하, 3: 좌
DIRS = [[0, -1], [1, 0], [0, 1], [-1, 0]]

BOARD_SIZE, RUNNER_CNT, TREE_CNT, ROUND_CNT = map(int, input().split(" "))


# 플레이어: 플레이어 -> 좌표, 좌표 -> 플레이어
taggerPosIdx = 0
taggerRoute = None
runners = [None]
deadRunners = [False for _ in range(RUNNER_CNT + 1)]
for _ in range(RUNNER_CNT):
  mis = list(map(int, input().split(" ")))
  runners.append([mis[1], mis[0], mis[2]])
  
# 나무: 좌표 -> 나무
treeBoard = [[False for _ in range(BOARD_SIZE + 1)] for _ in range(BOARD_SIZE + 1)]
for _ in range(TREE_CNT):
  mis = list(map(int, input().split(" ")))
  treeBoard[mis[0]][mis[1]] = True
  
  
# 함수
# print(runners)
# print(treeBoard)

def distance(x1, y1, x2, y2):
  return abs(x1-x2) + abs(y1-y2)
  
  
def isOutOfBoard(x, y):
  return x < 1 or y < 1 or x > BOARD_SIZE or y > BOARD_SIZE

# 1. m 명의 도망자 이동
# 술래와의 거리가 3 이하인 도망자만 움직임
#   거리 = x1-x2 + y1-y2
  
#   이동
#     현재 바라보고 있는 방향
#       격자를 벗어나지 않는 경우
#         술래가 있으면 움직이지 않음
#         술래가 있지 않으면 이동 (나무 있어도 가능)
        
#       격자를 벗어나는 경우
#         방향을 반대로 회전
#         바라보고 있는 방향으로 1칸 움직였을 때 술래 없다면 이동
def moveRunners():
  tagger = taggerRoute[taggerPosIdx]
  for ri in range(1, RUNNER_CNT+1):
    if deadRunners[ri]: continue
    x, y, d = runners[ri]
    distanceWithTagger = distance(x, y, tagger[0], tagger[1])
    if distanceWithTagger > 3: continue
    
    dx, dy = DIRS[d]
    nx, ny = x + dx, y + dy
    if isOutOfBoard(nx, ny):
      runners[ri][2] = (d + 2) % 4
      nx, ny = x - dx, y - dy
    if nx == tagger[0] and ny == tagger[1]: continue
    
    runners[ri][0], runners[ri][1] = nx, ny
    
    
    
# 2. 술래 이동
#   달팽이 모양으로 이동
#   끝에 도달하면 다시 거꾸로 중심으로 이동
  
#   이동 후 위치가 이동방향이 틀어지는 지점이면 방향 바로 틈
def getSnailRoute():
  route = []
  x, y = math.ceil(BOARD_SIZE/2), math.ceil(BOARD_SIZE/2)
  d, ci, f = 0, 0, 0
  circleCnt = BOARD_SIZE // 2
    
  for ci in range(1, circleCnt+1):
    # 빙글
    f = ci * 2 - 1
    for d in range(4):
      dx, dy = DIRS[d]
      for _ in range(f):
        route.append([x, y])
        x = x + dx
        y = y + dy
      if (d == 1): f += 1
  
  d = 0
  dx, dy = DIRS[d]
  for _ in range(f):
    route.append([x, y])
    x = x + dx
    y = y + dy
  
  route.append([x, y])
  return route

def getRoundSnailRoute():
  straightRoute = getSnailRoute()
  reverseRoute = copy.deepcopy(straightRoute)
  reverseRoute.reverse()
  straightRoute.extend(reverseRoute[1:-1])
  res = straightRoute
  
  # 0: 상, 1: 우, 2: 하, 3: 좌
  for i in range(len(res) - 1):
    cx, cy = res[i]
    nx, ny = res[i+1]
    dir = None
    if cy - 1 == ny: dir = 0
    elif cy + 1 == ny: dir = 2
    elif cx + 1 == nx: dir = 1
    elif cx - 1 == nx: dir = 3
    res[i].append(dir)
  res[-1].append(0)
  return straightRoute
  
def tagRunner(x, y):
  res = []
  if treeBoard[y][x] == True: return res
  for ri in range(1, RUNNER_CNT+1):
    if deadRunners[ri]: continue
    rx, ry = runners[ri][0], runners[ri][1]
    if (rx, ry) == (x, y): res.append(ri)
  
  return res
    



    
taggerRoute = getRoundSnailRoute()
# print(taggerRoute)


# 메인
# k번 반복
res = 0
for round in range(1, ROUND_CNT+1):
  moveRunners()
  # print("runners", runners[1])
  # print(taggerRoute[taggerPosIdx])
  # print(abs(runners[1][0] - taggerRoute[taggerPosIdx][0]), abs(runners[1][0] - taggerRoute[taggerPosIdx][0]))
  # 턴 넘기기 전에 시야 내에 있는 도망자 잡음
  # 술래의 시아 = 현재 바라보는 방향 포함하여 3칸
  #   나무 놓여 있는 칸이면 안잡힘

  # 잡힌 도망자는 사라짐.
  # 술래는 (턴 t * 현재 턴에서 잡은 도망자 수) 점수 얻음
  taggerPosIdx = (taggerPosIdx + 1) % len(taggerRoute)
  tagger = taggerRoute[taggerPosIdx]
  tx, ty, td = tagger
  dx, dy = DIRS[td]
  # print(tagger)
  for di in range(3):
    wx, wy = tx + dx * di, ty + dy * di
    if isOutOfBoard(wx, wy): continue
    taggedRunner = tagRunner(wx, wy)
    for taggedRunnerIdx in taggedRunner:
      deadRunners[taggedRunnerIdx] = True
      res += round
    
print(res)
