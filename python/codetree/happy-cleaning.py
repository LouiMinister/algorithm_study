# 청소는 즐거워

# n * n 행렬, n은 항상 홀수
# 정가운데에는 먼지 존재 X

# 정가운데 시작하여 나선형으로 바닥 청소

# 왼, 하, 우, 상 순서로 이동
# 항상 왼쪽 위에서 끝남

# 빗자루 도착지점의 먼지가 다른 공간으로 이동함
# a = Curr 먼지 - 이동된 먼지 (겪자 밖으로 던져진거 까지 포함)

# 겪자 바깥으로 나간 먼지의 양 출력

DIRS = [[-1, 0], [0, 1], [1, 0], [0, -1]]

N = int(input())
board = [[None for _ in range(N + 1)]]
for _ in range(N):
  board.append([None, *map(int, input().strip().split(" "))])
  
dustsOutOfBoard = 0
# 함수

def isOutOfBoard(x, y):
  return x < 1 or y < 1 or x > N or y > N

def snail():
  circles = N // 2
  
  force = 0  
  dx, dy = None, None
  for ci in range(circles):
    force += 1
    for _ in range(force): yield [*DIRS[0], 0]
    for _ in range(force): yield [*DIRS[1], 1]
    force += 1
    for _ in range(force): yield [*DIRS[2], 2]
    for _ in range(force): yield [*DIRS[3], 3]
  for _ in range(force): yield [*DIRS[0], 0]
  
# for x, y in snail():
#   print(x, y)

def spinSpread(x, y, percent, dir):
    if dir == 0: return [x, y, percent]
    if dir == 1: return [y, -x, percent]
    if dir == 2: return [-x, -y, percent]
    if dir == 3: return [-y, x, percent]

def dustSpread(dir):
  spreads = [[-2, 0, 5], [-1, -1, 10], [-1, 1, 10], [0, -2, 2], [0, 2, 2], [0, -1, 7], [0, 1, 7], [1, 1, 1], [1, -1, 1]]
  for spread in spreads:
    yield spinSpread(*spread, dir)
  
def lastDustSpread(dir):
  return spinSpread(-1, 0, 0, dir)


def sweep(x, y, dir):
  global board, dustsOutOfBoard
  dusts = board[y][x]
  leftDusts = dusts
  for sx, sy, percent in dustSpread(dir):
    nx, ny = x + sx, y + sy
    spreadDust = dusts * percent // 100
    leftDusts -= spreadDust
    if isOutOfBoard(nx, ny):
      dustsOutOfBoard += spreadDust
    else:
      board[ny][nx] += spreadDust
  lastSpread = lastDustSpread(dir)
  nx, ny = x + lastSpread[0], y + lastSpread[1]
  if isOutOfBoard(nx, ny):
    dustsOutOfBoard += leftDusts
  else:
    board[ny][nx] += leftDusts

def clean():
  x, y = N//2 + 1, N//2 + 1
  
  for dx, dy, dir in snail():
    x, y = x + dx, y + dy
    # print(x, y, dir)
    sweep(x, y, dir)
    
clean()

print(dustsOutOfBoard)
