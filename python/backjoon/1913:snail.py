import math

N = int(input())
willFindNum = int(input())
maxLev = (N + 1) // 2

SX = maxLev - 1
SY = maxLev - 1
MX = maxLev - 1
MY = maxLev - 1

ansX, ansY = MX, MY
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

board = [[0 for _ in range(N)] for _ in range(N)]
board[MY][MX] = 1
# 찾는게 1일 때 경우 처리


num = 2
for lv in range(2, maxLev+1):
  x, y = MX + 1 - lv, MY + 1 - lv
  steps = (lv - 1) * 2
  for dID in range(4):
    for i in range(1, steps + 1):
      x += dx[dID]
      y += dy[dID]
      if (willFindNum == num):
        ansX, ansY = x, y
      board[y][x] = num
      num += 1

for j in range(N):
  print(" ".join(map(str,board[j])))
print(f"{ansY+1} {ansX+1}")

