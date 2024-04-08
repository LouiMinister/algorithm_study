# 꼬리잡기놀이

# n * n 격자
# 머리사람: 맨 앞
# 꼬리사람: 맨 뒤

# 라운드
# 1. 머리사람을 따라 한 칸 이동
# 2. 
# ((ROUND - 1) % BOARD_SIZE + 1)

# 3. 공이 던저질 때 최초에 만나게 되는 사람만이 공을 얻게되어 점수를 얻음
# 머리사람을 시작으로 팀 내에서 k 번째 사람 -> k 제곱만큼의 점수
# 아무도 못받으면 점수 없음
# 공을 획득하면 방향이 바뀜(머리, 꼬리 사람 바뀜)
from collections import deque
import copy

# 상 우 하 좌
DIRS = [[0, -1], [1, 0], [0, 1], [-1, 0]]

BOARD_SIZE, TEAM_CNT, ROUND_CNT = map(int, input().split(" "))
EMPTY, HEAD, MID, TAIL, LINE = 0, 1, 2, 3, 4

# 0: 빈칸, 1: 머리, 2: 중간, 3: 꼬리, 4: 이동선
board = [[None for _ in range(BOARD_SIZE + 1)]]
heads = [None]
mids = [[] for _ in range(TEAM_CNT + 1)]
tails = [None for _ in range(TEAM_CNT + 1)]
for y in range(1, BOARD_SIZE+1):
  row = [None, *map(int, input().strip().split(" "))]
  for x in range(1, BOARD_SIZE+1):
    if row[x] == HEAD: heads.append([x, y]) 
  board.append(row)
# 각 팀이 획득한 점수의 총합
teamScores = [0 for _ in range(TEAM_CNT + 1)]


        


# 팀은 항상 3명 이상
# 유저 위치 찾아서 이동시키게 하고 다음 유저도 이동 시키고
# 헤드 위치는 계속 쫒아가게 하는게 좋을듯
# 루트에 사람이 꽉 차는 경우 주의! (덮어쓰기 문제)



# 함수
def isOutOfBoard(x, y):
  return x < 1 or y < 1 or x > BOARD_SIZE or y > BOARD_SIZE

def printBoard():
  for i in range(1, BOARD_SIZE + 1):
    print(board[i][1:])
    
def initTails():
  global tails
  for hi, head in enumerate(heads[1:], start=1):
    vis = [[False for _ in range(BOARD_SIZE + 1)] for _ in range(BOARD_SIZE + 1)]
    x, y = head
    vis[y][x] = True
    tail = None
    
    while True:
      # print("LOOP")
      for dx, dy in DIRS:
        nx, ny = x + dx, y + dy
        if isOutOfBoard(nx, ny): continue
        if vis[ny][nx]: continue
        vis[ny][nx] = True
        if board[ny][nx] == TAIL:
          if [x, y] == head: 
            vis[ny][nx] = False
            continue
          tail = [nx, ny]
          break
        if board[ny][nx] == MID:
          mids[hi].append([nx, ny])
          x, y = nx, ny
          break
      if tail != None:
        tails[hi] = tail
        break
    
# 머리 꼬리 붙은 경우 제외
def moveTeam():
  global board, heads, mids, tails
  nBoard = copy.deepcopy(board)
  for ti, head in enumerate(heads[1:], start=1):
    # head
    isCircle = False
    nHead, nMid, nTail = None, [], None
    hx, hy = head
    for dx, dy in DIRS:
      nx, ny = hx + dx, hy + dy
      if isOutOfBoard(nx ,ny): continue
      if board[ny][nx] == TAIL: 
        isCircle = True
        nBoard[ny][nx] = HEAD
        nHead = [nx, ny]
      if board[ny][nx] == LINE:
        nBoard[ny][nx] = HEAD
        nHead = [nx, ny]
    
    # mid
    midAry = mids[ti]
    for mi, mid in enumerate(midAry):
      if mi == 0:
        nMid.append(head)
        nBoard[hy][hx] = MID
      else:
        prevMid = midAry[mi-1]
        nMid.append(prevMid)
        nBoard[prevMid[1]][prevMid[0]] = MID #CHK
    
    # tail
    tx, ty = tails[ti]
    nTail = midAry[-1]
    nBoard[nTail[1]][nTail[0]] = TAIL
    if not isCircle:
      nBoard[ty][tx] = LINE
      
    heads[ti] = nHead
    mids[ti] = nMid
    tails[ti] = nTail
  board = nBoard    
    
def swapHeadTail(teamIdx):
  global heads, tails, mids, board
  heads[teamIdx], tails[teamIdx] = tails[teamIdx], heads[teamIdx]
  headPos = heads[teamIdx]
  board[headPos[1]][headPos[0]] = HEAD
  tailPos = tails[teamIdx]
  board[tailPos[1]][tailPos[0]] = TAIL
  mids[teamIdx].reverse()

def getTeamIdxAndGrade(x, y):
  for ti in range(1, TEAM_CNT + 1):
    grade = 1
    if heads[ti] == [x, y]:
      return [ti, grade]
    grade += 1
    
    for midPos in mids[ti]:
      if midPos == [x, y]:
        return [ti, grade]
      grade += 1
    
    if tails[ti] == [x, y]:
      return [ti, grade]
  
def throwBall(round):
  # d = 1~n: 우, n+1~2n: 상, 2n+1~3n: 좌, 3n+1~4n: 하
  sx, sy = None, None
  lineIdx = (round - 1) % BOARD_SIZE + 1
  lineType = ((round-1) // BOARD_SIZE) % 4
  
  if lineType == 0:
    sx, sy = 1, lineIdx
  elif lineType == 1:
    sx, sy = lineIdx, BOARD_SIZE
  elif lineType == 2:
    sx, sy = BOARD_SIZE, BOARD_SIZE - (lineIdx - 1) 
  elif lineType == 3:
    sx, sy = BOARD_SIZE - (lineIdx -1), 1
  
  lineDirs = [[1, 0], [0, -1], [-1, 0], [0, 1]]
  dir = lineDirs[lineType]
  for d in range(BOARD_SIZE):
    nx, ny = sx + dir[0] * d, sy + dir[1] * d
    # print("LINE: ", nx, ny)
    if board[ny][nx] == 1 or board[ny][nx] == 2 or board[ny][nx] == 3:
      return([nx, ny])
  
  return None
      
def ballHitAction(x, y):
  teamIdx, grade = getTeamIdxAndGrade(x, y)
  teamScores[teamIdx] += grade ** 2
  swapHeadTail(teamIdx) 
     
    
initTails()


for round in range(1, ROUND_CNT+1):
  moveTeam()
  ballHitPos = throwBall(round)
  if ballHitPos != None:
    ballHitAction(ballHitPos[0], ballHitPos[1])
  
print(sum(teamScores[1:]))

# for _ in range(4):
#   printBoard()
#   print("HEADS :", heads)
#   print("MIDS: ", mids)
#   print("TAILS: ", tails)
#   moveTeam()
  
# printBoard()
# print("HEADS :", heads)
# print("MIDS: ", mids)
# print("TAILS: ", tails)
# swapHeadTail(1)
# swapHeadTail(2)
# printBoard()
# print("HEADS :", heads)
# print("MIDS: ", mids)
# print("TAILS: ", tails)
# swapHeadTail(1)
# swapHeadTail(2)
# printBoard()
# print("HEADS :", heads)
# print("MIDS: ", mids)
# print("TAILS: ", tails)
# # print(board)

# print("THROW BALL")
# print(getTeamIdxAndGrade(1, 3))
# print(getTeamIdxAndGrade(2, 3))
# print(getTeamIdxAndGrade(3, 3))
# print("")

# print(getTeamIdxAndGrade(7, 2))
# print(getTeamIdxAndGrade(7, 3))
# print(getTeamIdxAndGrade(7, 4))
# print(getTeamIdxAndGrade(7, 5))
