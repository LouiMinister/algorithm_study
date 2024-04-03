# N x M 격자. 포탑의 개수는 NM개
# (y, x)


# 레이저 4방

from collections import deque
import copy

H, W, R = map(int, input().split(" "))
TURRET_CNT = H*W

# 보드
board = [[None for _ in range(W + 1)]]
for _ in range(H):
  board.append([None, *map(int, input().split(" "))])

# 포탑별 가장 최근에 공격한 턴
atkRoundPerTurret = [0 for _ in range(TURRET_CNT + 1)]

# 함수


def boardPosIter():
  for y in range(1, H + 1):
    for x in range(1, W + 1):
      yield (x, y)

def printBoard():
  for y in range(1, H + 1):
    print(board[y][1:])

# printBoard()

# 이동시 반대편 나오는거 고려한 좌표 이동 함수
def transPos(x, y):
  return [((x - 1 + W) % W) + 1, ((y - 1 + H) % H) + 1] 

# 약포
#   공격력 제일 낮음
#   가장 최근에 공격한 포탑
#   포탑 위치의 행 + 열이 가장 큰 포탑
#   열 값이 가장 큰 포탑

# 강포
#   공격력 가장 높음
#   공격한지 가장 오래된 포탑
#   행과 열의 합이 가장 작은 포탑
#   열 값이 가장 작은 포탑
def getTurretIdx(x, y):
  return (y - 1) * W + x

def getTurretsAry():
  ary = []
  for x, y in boardPosIter():
    turretIdx = getTurretIdx(x, y)
    dmg = board[y][x]
    if dmg <= 0: continue
    recentAtkRound = atkRoundPerTurret[turretIdx]
    ary.append(((dmg, -recentAtkRound, -(x+y), -x), [x, y])) # CHK: 열 값
  return ary

def getWorstTurret():
  ary = getTurretsAry()
  ary.sort()
  return ary[0][1]

def getBestTurret(exceptX, exceptY):
  ary = getTurretsAry()
  ary.sort(reverse=True)
  if ary[0][1] == [exceptX, exceptY]: # CHK: 조건 확인
    return ary[1][1]
  else:
    return ary[0][1]
  
def FDirIter(x, y):
  for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
    yield [x + dx, y + dy]
  

#     공격자의 위치에서 공격 대상까지 최단 경로로 공격.
#       최단 경로 두개면 - 우/하/좌/상 순서대로 먼저 움직인 경로 선택 (좌표 순서대로 bfs)
#       경로 정해지면, 공격자 공격력만큼 피해
#       피해 입으면 해당 수치만큼 공격력 감소
#       레이저 경로에 있는 포탑도 공격자 공격력//2 나눈 몫만큼 공격력삼소
#       존재하지 않으면 포탄 공격 진행

def getShortestPath(x1, y1, x2, y2):
  vis = [[False for _ in range(W+1)] for _ in range(H+1)]
  vis[y1][x1] = True
  paths = deque()
  paths.append([[x1, y1]])
  
  while paths:
    path = paths.popleft()
    lastPos = path[len(path) -1]
    for nx, ny in FDirIter(*lastPos):
      nx, ny = transPos(nx, ny)
      if board[ny][nx] <= 0: continue
      if vis[ny][nx]: continue
      vis[ny][nx] = True
      nPath = copy.deepcopy(path)
      nPath.append([nx, ny])
      paths.append(nPath)
      # print("NXNY", nx, ny)
      
      if (nx, ny) == (x2, y2):
        return nPath
  return None

def countAliveTurrets():
  cnt = 0
  for x, y in boardPosIter():
    if board[y][x] > 0: cnt += 1
  return cnt
  
# 포탑에는 공격력 존재. 0이하가 되면 부숴지고 공격 못함
# 최초에 0인 포탑이 존재 가능(부숴진 포탑)

# 4개의 액션, K번 반복
# 부셔지지 않은 포탑이 하나 되면 즉시 중지


  

  

  


# main
  
# R = 2
for r in range(1, R + 1):
  # 하나만 살아남으면 끝
  if countAliveTurrets() == 1:
    break
    
  # 1. 1보다 크거나 같은 포탑중 가장 약한 포탑이 공격자
  # N+M만큼 공격력 증가
  effectedTurrets = set()
  
  worstTurretPos = getWorstTurret()
  atkRoundPerTurret[getTurretIdx(worstTurretPos[0], worstTurretPos[1])] = r
  board[worstTurretPos[1]][worstTurretPos[0]] += H+W
  worstTurretDmg = board[worstTurretPos[1]][worstTurretPos[0]]
  effectedTurrets.add((worstTurretPos[0], worstTurretPos[1]))
  
  # 2. 자신 제외 가장 강한 포탑 공격
  
  #   레이저 공격
  #     상하좌우 4방향
  #     부서진 포탑 있는 위치는 지날 수 없음
  #     막힌 방향으로 이동하면 반대편으로 나옴
      
  #     공격자의 위치에서 공격 대상까지 최단 경로로 공격.
  #       최단 경로 두개면 - 우/하/좌/상 순서대로 먼저 움직인 경로 선택 (좌표 순서대로 bfs)
  #       경로 정해지면, 공격자 공격력만큼 피해
  #       피해 입으면 해당 수치만큼 공격력 감소
  #       레이저 경로에 있는 포탑도 공격자 공격력//2 나눈 몫만큼 공격력삼소
  #       존재하지 않으면 포탄 공격 진행
        
  #   포탄 공격
  #     공격자 공격력만큼 피해 + 주변 8방향은 공격자 공격력 절반 만큼의 피해
  #     공격자는 해당 공격에 영향 X
  #     가장자리에 떨어지면, 반대편 격자에 영향
  bestTurretPos = getBestTurret(*worstTurretPos)
  razerPath = getShortestPath(*worstTurretPos, *bestTurretPos) # CHK: 자신 치는지
  
  if razerPath == None:
    # 포탄 공격
    for dx, dy in [[0,-1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1]]:
      nx, ny = bestTurretPos[0] + dx, bestTurretPos[1] + dy
      nx, ny = transPos(nx, ny)
      if nx == worstTurretPos[0] and ny == worstTurretPos[1]: continue
      board[ny][nx] -= worstTurretDmg//2
      effectedTurrets.add((nx, ny))
    board[bestTurretPos[1]][bestTurretPos[0]] -= worstTurretDmg
    effectedTurrets.add((bestTurretPos[0], bestTurretPos[1]))
      
  else:
    # 레이저 공격
    if (len(razerPath) <=1): print("레이저길이", len(razerPath))
    for x, y in razerPath[1:-1]:
      board[y][x] -= worstTurretDmg//2
      effectedTurrets.add((x, y))
      
    lastRazerPos = razerPath[-1]
    board[lastRazerPos[1]][lastRazerPos[0]] -= worstTurretDmg
    effectedTurrets.add((lastRazerPos[0], lastRazerPos[1]))
  
  # print("WORST", worstTurretPos)
  # print("BEST", bestTurretPos)
  # print("ATK")
  # printBoard()
    
  # 3. 포탑 부서짐
  #   공격력 0이하가 된 포탑은 부서짐 # CHK: 0 이하 포탑 관리
  
  # 4. 공격과 무관한 포탑은 공격력 1씩 올라감. (공격자도 아니고, 공격에 피해를 입지 않은 포탑)
  for x, y in boardPosIter():
    if (x,y) in effectedTurrets: continue
    if board[y][x] <= 0: continue
    board[y][x] += 1
      
  # print("LEVEL UP")
  # printBoard()
  
  
  
maxDmg = 0
for x, y in boardPosIter():
  maxDmg = max(maxDmg, board[y][x])
  
print(maxDmg)
