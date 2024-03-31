# 왕실의 기사 대결



# 오답노트

# 재귀로 푸는 경우 한 블럭이 평행한 블럭 여러개를 밀었을 때 그중 한 줄기는 밀리고 한 줄기는 안밀리는 경우가 생기더라...
# 그래서 결국 첨에 이게 다 밀리는지 안밀리는지 확인을 하고나서 미는 작업을 해야함

# L x L 체스판 (1부터 시작)
# 빈칸 or 함정 or 벽 (체스판 밖도 벽)

# (y, x) 로 위치 주어짐
# h * w 크기의 직가삭형 형태
# k 체력


# 기사 이동

# 이동하려는 위치에 다른 기사 있으면 연쇄적으로 밀림
# 끝 기사 방향 끝에 벽 있으면 이동 불가


# 대결 대미지

# 밀려난 기사는 피해를 입게 됨
# w x h 직사각형 내에 놓아있는 함정 갯수만큼 피해 (밀려진 위치에 함정 없으면 피해 X)
# 현재 체력 이상의 대미지 -> 체스판에서 사라짐
# 명령을 받은 기사는 피해 X, 모두 밀린 이후에 대미지

# Q번에 걸친 왕의 명령

# with open("asd.txt",'w') as f:

DIR = [[0, -1], [1, 0], [0, 1], [-1, 0]]

BOARD_SIZE, KNIGHTS_CNT, COMMANDS_CNT = map(int, input().split(" "))

board = [[-1 for _ in range(BOARD_SIZE + 1)]]
knightBoard = [[0 for _ in range(BOARD_SIZE + 1)] for _ in range(BOARD_SIZE + 1)]
for _ in range(BOARD_SIZE):
  board.append([-1, *map(int, input().split(" "))])

knights = [None]
for knightIdx in range(KNIGHTS_CNT):
  mis = list(map(int, input().split(" ")))
  knights.append({
    "x": mis[1],
    "y": mis[0],
    "h": mis[2],
    "w": mis[3],
    "hp": mis[4],
    "dmg": 0,
  })
  
  for hi in range(mis[2]):
    for wi in range(mis[3]):
      knightBoard[mis[0] + hi][mis[1] + wi] = knightIdx+1
  
# print(knights)
# print(knightBoard)
# print(board)

def isWall(x, y):
  return x <= 0 or y <= 0 or x > BOARD_SIZE or y > BOARD_SIZE or board[y][x] == 2

def eraseKnight(knightIdx):
  knight = knights[knightIdx]
  curX, curY = knight["x"], knight["y"]
  for hi in range(knight["h"]):
    for wi in range(knight["w"]):
      knightBoard[curY + hi][curX + wi] = 0
      # print(curX + wi, curY + hi)
      
      

def canMove(knightIdx, dir):
  knight = knights[knightIdx]
  if knight["hp"] <= 0: return False
  curX, curY = knight["x"], knight["y"]
  
  collidedKnights = set()
  
  for hi in range(knight["h"]):
    for wi in range(knight["w"]):
      nextX, nextY = curX + wi + dir[0], curY + hi + dir[1]
      if isWall(nextX, nextY): # 벽이면
        return False
      cell = board[nextY][nextX]
      knightCell = knightBoard[nextY][nextX]
      if knightCell != 0 and knightCell != knightIdx:
        collidedKnights.add(knightCell)
  
  # 움직였을 때 다음 나이트 이동.
  # 만약 다음 나이트 이동 결과 return False 라면 False
  for collidedKnight in collidedKnights:
    isChainMoveSuccess = canMove(collidedKnight, dir)
    if not isChainMoveSuccess:
      return False
    
  return True


isMoved = [False for _ in range(KNIGHTS_CNT + 1)]
deadKnights = []
def moveKnight(knightIdx, dir, isSelf):
  if isMoved[knightIdx]: 
    return True
  isMoved[knightIdx] = True
  
  knight = knights[knightIdx]
  if knight["hp"] <= 0: return True
  curX, curY = knight["x"], knight["y"]
  damages = 0
  collidedKnights = set()
  
  # 움직인 곳에 벽이 있는 경우 return False
  for hi in range(knight["h"]):
    for wi in range(knight["w"]):
      nextX, nextY = curX + wi + dir[0], curY + hi + dir[1]
      if isWall(nextX, nextY): # 벽이면
        return False
      cell = board[nextY][nextX]
      knightCell = knightBoard[nextY][nextX]
      # print("ISWALL", knightIdx, isWall(nextX, nextY))
      if not isSelf and cell == 1: # 함정 있으면
        damages += 1
      if knightCell != 0 and knightCell != knightIdx:
        collidedKnights.add(knightCell)
  
  # 움직였을 때 다음 나이트 이동.
  # 만약 다음 나이트 이동 결과 return False 라면 False
  for collidedKnight in collidedKnights:
    isChainMoveSuccess = moveKnight(collidedKnight, dir, False)
    if not isChainMoveSuccess:
      return False
  
  # 데미지 업데이트
  knights[knightIdx]["hp"] -= damages
  knights[knightIdx]["dmg"] += damages
  if knights[knightIdx]["hp"] <= 0:
    # print("ERASE", knightIdx)
    deadKnights.append(knightIdx)
    return True
  
  # 이동 후 현재 위치 업데이트
  for hi in range(knight["h"]):
    for wi in range(knight["w"]):
      prevX, prevY = curX + wi, curY + hi
      knightBoard[prevY][prevX] = 0
      
  for hi in range(knight["h"]):
    for wi in range(knight["w"]):
      nextX, nextY = curX + wi + dir[0], curY + hi + dir[1]
      knightBoard[nextY][nextX] = knightIdx
      
  knights[knightIdx]["x"] = curX + dir[0]
  knights[knightIdx]["y"] = curY + dir[1]
  return True

# for i in range(1, BOARD_SIZE+1):
#   print(knightBoard[i][1:], file=f)
  
# print("", file=f)

for _ in range(COMMANDS_CNT):
  mis = list(map(int , input().split(" ")))
  knightIdx = mis[0]
  dir = DIR[mis[1]]
  isMoved = [False for _ in range(KNIGHTS_CNT + 1)]
  deadKnights = []
  # print(knightIdx, dir, file=f)
  if canMove(knightIdx, dir):
    moveKnight(knightIdx, dir, True)
    for deadKnight in deadKnights:
      eraseKnight(deadKnight)
    
  # for i in range(1, BOARD_SIZE+1):
  #   print(knightBoard[i][1:], file=f)
    
  # print("", file=f)
  

res = 0
for knight in knights[1:]:
  if knight["hp"] > 0:
    res += knight["dmg"]

# print(knights)
# for knight in knights:
#   print(knight, file=f)
print(res)

