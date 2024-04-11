# n * n 격자 칸
# 서로 다른 높이의 나무

  






# 1년동안의 단계
# 1. 특수 영양제를 이동 규칙에 따라 이동

  
# 결과: 해당 년수가 모두 지나고 난 뒤 남아있는 나무 높이들의 총 합

# 1~8임
from copy import deepcopy

DIRS = [[1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1]]

BOARD_SIZE, YEARS = map(int, input().split(" "))
board = [[None for _ in range(BOARD_SIZE + 1)]]
for _ in range(BOARD_SIZE):
  board.append([None, *map(int, input().strip().split(" "))])

# 초기 특수 영양제: 좌 하단 4개의 칸
growths = [[False for _ in range(BOARD_SIZE + 1)] for _ in range(BOARD_SIZE + 1)]
growths[BOARD_SIZE][1] = True
growths[BOARD_SIZE-1][1] = True
growths[BOARD_SIZE][2] = True
growths[BOARD_SIZE-1][2] = True

# 함수

# 행, 열은 각각 끝 끝 연결
def calibratePos(x, y):
  return (((x -1) % BOARD_SIZE) + 1, ((y -1) % BOARD_SIZE) + 1)

def boardIter():
  for y in range(1, BOARD_SIZE + 1):
    for x in range(1, BOARD_SIZE + 1):
      yield(x, y)


def printGrowths():
  print("PRINT GROWTH")
  for y in range(1, BOARD_SIZE + 1):
    print(growths[y][1:])
    
def printBoard():
  print("PRINT BOARD")
  for y in range(1, BOARD_SIZE + 1):
    print(board[y][1:])
    
def isOutOfBoard(x, y):
  return x < 1 or y < 1 or x > BOARD_SIZE or y > BOARD_SIZE

# 특수 영양제 이동 규칙
# 이동 방향: 우, 우상, 상 으로 반시계계 8방향
# 이동 칸 수만큰 이동
def moveGrowths(dir, dist):
  global growths
  nGrowth = [[False for _ in range(BOARD_SIZE + 1)] for _ in range(BOARD_SIZE + 1)]
  dx, dy = DIRS[dir]
  # print("DXDY", dx, dy)

  for x, y in boardIter():
    nx, ny = calibratePos(x + dx * dist, y + dy * dist)    
    nGrowth[ny][nx] = growths[y][x]
  growths = nGrowth
  
# 2. 이동 시킨 후 해당 땅에 영양제 투입.
#   투입 후 땅에 있던 특수 영양제는 사라짐
# 3. 영양제를 투입한 나무의 대각선으로 인접한 방향의 높이가 1 이상의 나무가 있는 만큼 높이 더 성장
# 4. 영양제 투입 나무 제외 높이가 2 이상인 나무는 높이 2를 베어냄
#   해당 위치에 특수 영양제를 올려 둠
def growTrees():
  global board, growths
  nGrowths = [[False for _ in range(BOARD_SIZE + 1)] for _ in range(BOARD_SIZE + 1)]
  
  # growths 순회 하면서
  for x, y in boardIter():
  #   땅의 리브로수 높이 1 증가
  #   씨앗만 있으면 높이 1의 리브로수 생성
    if growths[y][x]:
      board[y][x] += 1
        
  nBoard = deepcopy(board)
  #   대각선으로 인접한 방향, 높이가 1 이상의 나무가 있는 만큼 더 성장
  for x, y in boardIter():
    #   땅의 리브로수 높이 1 증가
    if not growths[y][x]: continue
    for dx, dy in [[-1, -1], [-1, 1], [1, 1], [1, -1]]:
      nx, ny = x + dx, y + dy # CHK: 넘어가는거 조정해야할지
      if isOutOfBoard(nx, ny): continue
      if board[ny][nx] >= 1: 
        nBoard[y][x] += 1
        
  # print("GROW TREE LV1")
  # nBoard, board = board, nBoard
  # printBoard()
  # nBoard, board = board, nBoard
  
  # # nBoard 전체 칸 순회
  for x, y in boardIter():
  #   영양제 투입 칸 제외
    if growths[y][x]: continue
  #   높이가 2 이상인 나무는 2를 베어냄.
    if board[y][x] >= 2:
      nBoard[y][x] -= 2
  #   해당 위치에 영양제 올림
      nGrowths[y][x] = True
  
  growths = nGrowths
  board = nBoard
  # print("GROWTREES END")

def sumTree():
  res = 0
  for x, y in boardIter():
    res += board[y][x]
  return res

# printBoard()
# printGrowths()
# moveGrowths(0, 2)
# printGrowths()

for year in range(1, YEARS + 1):
  # print("")
  # print("YEAR: ", year)
  d, p = map(int, input().split(" "))
  moveGrowths(d-1, p)
  # printGrowths()
  growTrees()
  
  # printGrowths()
  # printBoard()
print(sumTree())
