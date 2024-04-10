# 정육면체 한번 더 굴리기


# 1~6 임의 숫자가 그려진 N*N 격자판
# 1*1 크기의 정육면체

# #   5
# # 4 1 3
# #   2
# #   6

# 격자판의 1행 1열에 놓여짐
# 처음에는 항상 오른쪽으로 이동

# 점수 획득
#   주사위 칸의 숫자와 상하좌우 인접하며 같은 숫자가 적혀있는 모든 칸의 합만큼 점수 획득
  
# 이동
#   구르는 방향에 맞게 주사위가 바라보는 면이 달라짐
#   주사위 아랫면 > 보드의 해당 칸 -> 진행방향 90 시계방향 회전
#   주사위 아랫면 < 보드의 해당 칸 -> 진행방향 90 반시계 회전
#   = -> 계속 현재 방향 지속
#   이후 구르기
#   굴렀을 때 격자 밖으로 가면 -> 반대로 한칸 이동 
  
from collections import deque

DIRS = [[1, 0], [0, 1], [-1, 0], [0, -1]]
BOARD_SIZE, ROLL_CNT = map(int, input().split())
board = [[None for _ in range(BOARD_SIZE + 1)]]
for _ in range(BOARD_SIZE):
  board.append([None, *map(int, input().strip().split(" "))])
               

def isOutOfBoard(x, y):
  return x < 1 or y < 1 or x > BOARD_SIZE or y > BOARD_SIZE
  
class Dice:
  # 윗면으로 시작해서 오른쪽 면
  x = 1
  y = 1
  row = deque([1, 3, 6, 4])
  # 윗면으로 시작해서 아랫쪽 면
  col = deque([1, 2, 6, 5])
  dir = 0
  
  def print(self):
    print(self.row)
    print(self.col)
    
  def _syncRowToCol(self):
    self.col[0] = self.row[0]
    self.col[2] = self.row[2]
    
  def _syncColToRow(self):
    self.row[0] = self.col[0]
    self.row[2] = self.col[2]
  
  def rollRight(self):
    self.row.appendleft(self.row.pop())
    self._syncRowToCol()
  
  def rollLeft(self):
    self.row.append(self.row.popleft())
    self._syncRowToCol()
    
  def rollUp(self):
    self.col.append(self.col.popleft())
    self._syncColToRow()
    
  def rollDown(self):
    self.col.appendleft(self.col.pop())
    self._syncColToRow()
    
  def move(self):
    
    dx, dy = DIRS[self.dir]
    nx, ny = self.x + dx, self.y + dy
    if isOutOfBoard(nx, ny):
      self.dir = (self.dir + 2) % 4
      self.move()
      return
    rollFuncs = [self.rollRight, self.rollDown, self.rollLeft, self.rollUp]
    rollFuncs[self.dir]()
    self.x, self.y = nx, ny
  
  def getUpwardNum(self):
    return self.col[0]
  
  def getDownwardNum(self):
    return self.col[2]
  
  def spinDir(self, d):
    self.dir = (self.dir + d) % 4
    
  #   구르는 방향에 맞게 주사위가 바라보는 면이 달라짐
  #   주사위 아랫면 > 보드의 해당 칸 -> 진행방향 90 시계방향 회전
  #   주사위 아랫면 < 보드의 해당 칸 -> 진행방향 90 반시계 회전
  def checkFloorNum(self):
    floorNum = board[self.y][self.x]
    downWardNum = self.getDownwardNum()
    if downWardNum > floorNum:
      self.dir = (self.dir + 1) % 4
    elif downWardNum < floorNum:
      self.dir = (self.dir - 1) % 4
    
def getBoardScore(x, y):
  global board
  vis = [[False for _ in range(BOARD_SIZE + 1)] for _ in range(BOARD_SIZE + 1)]
  vis[y][x] = True
  dq = deque()
  dq.append([x, y])
  floorNum = board[y][x]
  res = floorNum
  
  while dq:
    curX, curY = dq.popleft()
    for dx, dy in DIRS:
      nx, ny = curX + dx, curY + dy
      if isOutOfBoard(nx, ny): continue
      if vis[ny][nx]: continue
      vis[ny][nx] = True
      if board[ny][nx] != floorNum: continue
      res += floorNum
      dq.append([nx, ny])
  return res
      
res = 0
dice = Dice()  
for ri in range(1, ROLL_CNT+1):
  dice.move() 
  res += getBoardScore(dice.x, dice.y)
  # print("RES: ",res)
  dice.checkFloorNum()
print(res)
  
