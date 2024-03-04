

# 각 값 -> 라인 매핑
# ex) 11 -> 가로 0, 세로 0, 대각 0

row = [[] for _ in range(5)]
col = [[] for _ in range(5)]
drl = [] # 아래 대각
url = [] # 위 대각

lineMemo = {}

board = []
picks = []
for _ in range(5):
  board.append(list(map(int, input().split(' '))))
for _ in range(5):
  picks.append(list(map(int, input().split(' '))))

for j in range(5):
  for i in range(5):
    cell = board[j][i]
    lineMemo[cell] = [row[j], col[i]]

    if (i==j):
      lineMemo[cell].append(drl)
    if ((4-i) == j):
      lineMemo[cell].append(url)
      
def checkThreeBingo():
  bingoCnt = 0
  for i in range(5):
    if len(row[i]) >= 5: bingoCnt += 1
    if len(col[i]) >= 5: bingoCnt += 1
  if len(drl) >= 5: bingoCnt += 1
  if len(url) >= 5: bingoCnt += 1
  if bingoCnt >= 3: return True
  else: return False
      
def checkBingo(pick):
  lines = lineMemo[pick]
  for line in lines:
    line.append(pick)
  if checkThreeBingo():
    return True
  else:
    return False

def simul():
  tryCnt = 0
  for j in range(5):
      for i in range(5):
        tryCnt += 1
        pick = picks[j][i]
        res = checkBingo(pick)
        if res == True:
          print(tryCnt)
          return

simul()
