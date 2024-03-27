# 공 - 수
# 넘어뜨림 (4방) 

# 공격 - X행 Y열 D 방향
# D = E, W, S, N
# 수비 - X, Y

# 해당 라운드마다 넘어뜨린 도미노 개수 SUM

CMD = {
  'N': (0, -1),
  'E': (1, 0),
  'W': (-1,0),
  'S': (0,1)
}

Y, X, R = map(int, input().split(" "))

board = []
stand = []

def isInBoundary(x, y):
  return x >= 0 and y >= 0 and x < X and y < Y

def offense(x, y, d):
  global CMD, board
  if not isInBoundary(x, y): return 0
  
  score = 0
  # print(x, y, d)
  dx, dy = CMD[d]
  
  height = board[y][x]
  
  if stand[y][x]:
    stand[y][x] = False
    score += 1
    for i in range(1, height):
      nx, ny = x + i * dx, y + i * dy
      if not isInBoundary(nx, ny): break
      if stand[ny][nx]:
        score += offense(nx, ny, d)
  
  return score
    
    
  
def defense(x, y):
  stand[y][x] = True
  

for _ in range(Y):
  board.append(list(map(int, input().split(" "))))
  stand.append([True for _ in range(X)])


res = 0
for _ in range(R):
  cmd = input().split(" ")
  res += offense(int(cmd[1])-1, int(cmd[0])-1, cmd[2])
  # print("!!!!!!!!!!!!", res)
  # for s in stand:
    # print(s)
  # print(stand)
  cmd = input().split(" ")
  defense(int(cmd[1])-1, int(cmd[0])-1)
  
print(res)

def translate(s):
  if s == True:
    return "S"
  else:
    return "F"
  
for s in stand:
  print(" ".join(map(translate, s)))
