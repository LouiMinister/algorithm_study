

# 게임판
# (y,x) 형태 (r, c)

# M턴, - 턴마다 루돌프와 산타들이 한 번씩 움직임
# 루돌프 한번 움직임, 산타 1~P번까지 순서대로 움직임
# 기절, 격자밖 탈락 산타는 못움직임

def distance(x1, y1, x2, y2):
  return (x1-x2)**2 + (y1-y2)**2

# 루돌프 dx dy
rudolfDirs = [(1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1)]
# 산타 dx xy 상우하좌
santaDirs = [[0, -1], [1, 0], [0, 1], [-1, 0]]

WIDTH, ROUND, SANTA_CNT, RUDOLF_STR, SANTA_STR = map(int, input().split(" "))

tmp = list(map(int, input().split(" ")))
board = [[-1 for _ in range(WIDTH + 1)] for _ in range(WIDTH + 1)]
# 현재 루돌프 위치
rudolfPos = [tmp[1], tmp[0]]
board[tmp[0]][tmp[1]] = 0

# 현재 산타 위치
santaPos = [None for _ in range(SANTA_CNT + 1)]
santaAlive = [True for _ in range(SANTA_CNT + 1)]
for _ in range(SANTA_CNT):
  tmp = list(map(int, input().split(" ")))
  santaPos[tmp[0]] = [tmp[2], tmp[1]]
  board[tmp[1]][tmp[2]] = tmp[0]
  
# 스턴 지속시간
santaStunRemain = [0 for _ in range(SANTA_CNT + 1)]
# 산타별 점수
santaScore = [0 for _ in range(SANTA_CNT + 1)]

# 루돌프
#   가장 가까운 산타한테 1칸 돌진 (탈락하지 않은 산타 중)
#   가장 가까운 산타가 2명 이상 -> r 좌표가 큰, 같으면 c 좌표가 큰
#   8 방향중 한칸으로 이동

def isOutOfBoundary(x, y):
  global WIDTH
  return x < 1 or y < 1 or x > WIDTH or y > WIDTH

def getNearSantaDir(x, y):
  global santaPos, santaAlive
  santaDistances = []
  # TODO: 죽은 산타는 제외
  for santaIdx, pos in enumerate(santaPos[1:], start=1):
    if not santaAlive[santaIdx]: continue
    distance = (pos[0]-x)**2 + (pos[1]-y)**2
    santaDistances.append((distance, -pos[1], -pos[0], santaIdx))
  santaDistances.sort()
  # print("SANTADISTANCES", santaDistances)
  nearSantaPos = (-santaDistances[0][2], -santaDistances[0][1])
  
  moveDir = [nearSantaPos[0] - x, nearSantaPos[1] - y]
  moveDir = [max(min(moveDir[0], 1), -1), max(min(moveDir[1], 1), -1)] # 0/0 되나 확인
  # print("SANTAMOVEDIR", moveDir)
  
  return moveDir

def killSanta(i):
  curSantaPos = santaPos[i]
  board[curSantaPos[1]][curSantaPos[0]] = 0
  santaAlive[i] = False


#     밀리는 도중엔 충돌 X
#     도착 지점이 게임판 밖이면 산타 탈락
#     도착 지점에 다른 산타 있으면 상호작용

# 충돌
#   산타 루돌프 같은 칸 있으면 충돌
#   루돌프 이동 충돌시 산타는 C만큼 점수 get & 산타는 루돌프가 이동해온 방향으로 C칸만큼 밀림
#   산타 이동 충돌시 산타는 D만큼 점수 get & 산타는 자신이 이동해온 반대 방향으로 D칸만큼 밀림
#   산타는 루돌프와 충돌시 (k번째 턴이라면) (k+1) 번째 턴까지 기절. (k+2)번째 턴부터 다시 정상 상태

# 상호작용
#   이미 다른 산타 있다면 그 산타는 해당 방향으로 1칸 밀림. 거기에도 산타가 있으면 1칸씩 밀림 반복
#   게임판 밖으로 밀려난 산타는 탈락
def moveSanta(i, x, y, dir):
  # 현재 위치 삭제
  curSantaPos = santaPos[i]
  board[curSantaPos[1]][curSantaPos[0]] = -1
  # 도착한 곳이 외부면 사망
  if isOutOfBoundary(x, y):
    santaAlive[i] = False
    santaPos[i] = None
    # print("!!!!!!!!!!!!", x, y)
    return
  
  destinationNum = board[y][x]
  
  # if destinationNum == i: print("MOVESANTA ERROR!!!!") # TODO: 삭제요망
  # 도착한 곳이 산타면 재귀
  if destinationNum > 0:
    moveSanta(destinationNum, x + dir[0], y + dir[1], dir)
  # 도착한 곳이 루돌프면 
  elif destinationNum == 0:
    santaScore[i] += SANTA_STR
    # 자신이 이동해온 반대 방향으로 D칸만큼 밀림 = 현 위치에서 반대방향으로 -1칸만큼 이동
    dir = [-dir[0], -dir[1]]
    moveSanta(i, x + dir[0] * SANTA_STR, y + dir[1] * SANTA_STR, dir)
    santaStunRemain[i] = 2
    # print("@@@@@@@@@@@@@@@@@@")
    return
    
  
  # 보드, 산타 위치 업데이트
  santaPos[i] = [x, y]
  board[y][x] = i
  # print("MOVESANTA", i, x, y)


# 보드, 루돌프 위치 업데이트
# 충돌시
# 루돌프 이동 충돌시 산타는 C만큼 점수 get & 산타는 루돌프가 이동해온 방향으로 C칸만큼 밀림
#   산타는 루돌프와 충돌시 (k번째 턴이라면) (k+1) 번째 턴까지 기절. (k+2)번째 턴부터 다시 정상 상태
# 산타 기절

# 충돌 없을 시 끝
def moveRudolf(x, y, dir):
  global rudolfPos
  # 현재 위치 삭제
  # print("MOVERUDOLF", x, y)
  board[rudolfPos[1]][rudolfPos[0]] = -1
  destinationNum = board[y][x]
  
  # 도착한 곳이 산타면 충돌
  if destinationNum > 0:
    santaScore[destinationNum] += RUDOLF_STR
    moveSanta(destinationNum, x + dir[0] * (RUDOLF_STR), y + dir[1] * (RUDOLF_STR), dir)
    santaStunRemain[destinationNum] = 2
    
  rudolfPos = [x, y]
  board[y][x] = 0
  

# 충돌
#   산타 루돌프 같은 칸 있으면 충돌

#   산타 이동 충돌시 산타는 D만큼 점수 get & 산타는 자신이 이동해온 반대 방향으로 D칸만큼 밀림
#   산타는 루돌프와 충돌시 (k번째 턴이라면) (k+1) 번째 턴까지 기절. (k+2)번째 턴부터 다시 정상 상태
  
#     밀리는 도중엔 충돌 X
#     도착 지점이 게임판 밖이면 산타 탈락
#     도착 지점에 다른 산타 있으면 상호작용
def runRudolf():
  moveDir = getNearSantaDir(*rudolfPos)
  # print("RUNRUDOLF", moveDir)
  moveRudolf(rudolfPos[0] + moveDir[0], rudolfPos[1] + moveDir[1], moveDir)

# 산타
#   1~P 순서대로 이동
#   기절, 탈락한 산타는 움직임 X
#   루돌프에게 가장 가까워지는 방향으로 1칸 이동
#   다른 산타 or 게임판 밖 이동 x
#   움직일 수 있는 칸 X -> 움직임 x
#   움직일 수 있는 칸 있어도 가까워질 방법 X이면 움직임 X
#   상하좌우 4방. 가장 가까워지는 방향 여러개면 상우하좌 순서로

# 충돌
#   산타 루돌프 같은 칸 있으면 충돌
#   루돌프 이동 충돌시 산타는 C만큼 점수 get & 산타는 루돌프가 이동해온 방향으로 C칸만큼 밀림
#   산타 이동 충돌시 산타는 D만큼 점수 get & 산타는 자신이 이동해온 반대 방향으로 D칸만큼 밀림
#   산타는 루돌프와 충돌시 (k번째 턴이라면) (k+1) 번째 턴까지 기절. (k+2)번째 턴부터 다시 정상 상태
  
def getNearRudolfDir(x, y):
  curDistance = distance(x, y, rudolfPos[0], rudolfPos[1])
  minDistance = curDistance
  bestDir = None
  for dir in santaDirs:
    nx, ny = x + dir[0], y + dir[1]
    if isOutOfBoundary(nx, ny): continue
    if board[ny][nx] > 0: continue # 다른 산타 있는 경우
    
    nDistance = distance(nx, ny, rudolfPos[0], rudolfPos[1])
    if nDistance < minDistance:
      bestDir = [dir[0], dir[1]]
      minDistance = nDistance
    
  return bestDir
    
  

def runSanta():
  for i in range(1, SANTA_CNT + 1):
    if not santaAlive[i]: continue
    if santaStunRemain[i] > 0: continue
    
    moveDir = getNearRudolfDir(*santaPos[i])
    if moveDir != None:
      curSantaPos = santaPos[i]
      # print("RUNSANTA", i, curSantaPos[0] + moveDir[0], curSantaPos[1] + moveDir[1], moveDir)
      moveSanta(i, curSantaPos[0] + moveDir[0], curSantaPos[1] + moveDir[1], moveDir)
    
    
def isWholeSantaDead():
  for i in range(1, SANTA_CNT+1):
    if santaAlive[i]: return False
  return True

def printBoard():
  for i in range(1, WIDTH+1):
    print(board[i][1:])
  print("")
      

# printBoard()
for r in range(ROUND):
  for i in range(1, SANTA_CNT+1):
    santaStunRemain[i] = max(0, santaStunRemain[i]-1)
  
  # print("ROUND ",r)
  
  # print("santaScore", santaScore)
  # print("santaAlive", santaAlive)
  # print("santaStunRemain ",santaStunRemain)
  # print("santaPos", santaPos)
  runRudolf()
  # printBoard()
  runSanta()
  # printBoard()
  
  
  for i in range(1, SANTA_CNT+1):
    if santaAlive[i]:
      santaScore[i] += 1
  
  if isWholeSantaDead(): break
  
print(" ".join(map(str, santaScore[1:])))

