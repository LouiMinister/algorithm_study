# n * n 학생
# n * n 격자
# 순서대로 놀이기구 탑승

# 학생별로 좋아하는 학생이 4명씩
# 자기 자신 X
# 동일한 학생에 대해 좋아하는 학생 번호 중복일 수 X

# 입력으로 주어진 순서대로 다음 조건 우선순위 높은 칸을 ㅗ탑승
# 항상 비어있는 칸으로만 이동

# 1. 격자를 벗어나지 않는 4방 인접 칸 중 좋아하는 친구 수 가장 많은 위치로 

# 2. 1이 여러개면, 그 중 인접한 칸 중 비어있는 칸 수가 가장 많은 위치로 (격자 넘은 칸은 빈칸 X)

# 3. 2가 여러개면, 그 중 행(y)이 가장 작은 위치

# 4. 3이 여러개면, 그 중 열(x)이 가장 작은 위치

# 좋아하는 친구의 수 점수
# [0, 1, 10, 100, 1000]

# 모든 학생의 점수 합 반환

N = int(input())

board = [[0 for _ in range(N+1)] for _ in range(N+1)]
users = [None]
userFavors = [None for _ in range(N*N + 1)]

for _ in range(N*N):
  mis = list(map(int, input().strip().split(" ")))
  user, favors = mis[0], mis[1:]
  users.append(user)
  userFavors[user] = favors

def printBoard():
  for y in range(1, N + 1):
    print(board[y][1:])

def boardIter():
  for y in range(1, N+1):
    for x in range(1, N+1):
      yield (x, y)
      
def isOutOfBoard(x, y):
  return x < 1 or y < 1 or x > N or y > N

def getBestPos(favors):
  # [-인접 친구 수, -인접 빈칸 수, y, x]
  posCandis = []
  for x, y in boardIter():
    if board[y][x] != 0: continue
    nearFavors = 0
    nearSpaces = 0
    for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
      nx, ny = x + dx, y + dy
      if isOutOfBoard(nx, ny): continue
      if board[ny][nx] in favors:
        nearFavors += 1
      if board[ny][nx] == 0:
        nearSpaces += 1
    posCandis.append((-nearFavors, -nearSpaces, y, x))
  posCandis.sort()
  
  # print("posCandis", posCandis)
  
  return [posCandis[0][3], posCandis[0][2]]
  
    
def getScores():
  res = 0
  scoreBoard = [0, 1, 10, 100, 1000]
  for x, y in boardIter():
    user = board[y][x]
    favors = userFavors[user]
    nearFavors = 0
    for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
      nx, ny = x + dx, y + dy
      if isOutOfBoard(nx, ny): continue
      if board[ny][nx] in favors:
        nearFavors += 1
    res += scoreBoard[nearFavors]
  return res

  
for i in range(1, N*N + 1):
  user = users[i]
  favors = userFavors[user]
  # print("USER FAVOR", user, favors)
  bestPos = getBestPos(favors)
  # print("BEST POS", user, bestPos)
  board[bestPos[1]][bestPos[0]] = user
  
print(getScores())
# printBoard()
