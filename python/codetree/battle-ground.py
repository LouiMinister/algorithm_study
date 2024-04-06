# n * n 크기의 격자
# 격자엔 무기 존재

# 플레이어는 빈 격자에 존재 (처음에)
# 플레이어 - 초기 능력치 (모두 다름)

# 총 - 공격력
# 플레이어 - 번호, 초기 능력치

# 플레이어별 점수
DIRS = [[0, -1], [1, 0], [0, 1], [-1, 0]]

BOARD_SIZE, PLAYER_CNT, ROUND_CNT = map(int, input().split(" "))
board = [[None for _ in range(BOARD_SIZE + 1)]]
for _ in range(BOARD_SIZE):
  board.append([None, *map(lambda x: [] if x == "0" else [int(x)], input().split(" "))])

players = [None]
playerScores = [0 for _ in range(PLAYER_CNT + 1)]
for _ in range(PLAYER_CNT):
  y, x, dir, stat = list(map(int, input().split(" ")))
  players.append({
    "x": x,
    "y": y,
    "dir": dir,
    "stat": stat,
    "gun": 0,
  })
  

# 함수
def printBoard():
  for y in range(1, BOARD_SIZE+1):
    print(board[y][1:])
    

    
def printPlyer():
  for pi in range(1, PLAYER_CNT+1):
    print(players[pi])
    
def isOutOfBoard(x, y):
  return x < 1 or y < 1 or x > BOARD_SIZE or y > BOARD_SIZE

def getPlayerIdx(x, y, exceptPlayerIdx=None): # 개선 가능
  for pi in range(1, PLAYER_CNT+1):
    if pi == exceptPlayerIdx: continue
    player = players[pi]
    if player["x"] == x and player["y"] == y:
      return pi
  return None

def printBoardPlayer():
  pBoard = [[0 for _ in range(BOARD_SIZE + 1)] for _ in range(BOARD_SIZE + 1)]
  for y in range(1, BOARD_SIZE + 1):
    for x in range(1, BOARD_SIZE + 1):
      playerIdx = getPlayerIdx(x, y)
      if playerIdx != None:
        pBoard[y][x] = playerIdx

  for y in range(1, BOARD_SIZE+1):
    print(pBoard[y][1:])

def move(player):
    sx, sy = player["x"], player["y"]
    sDir = player["dir"]
    nx, ny = sx + DIRS[sDir][0], sy + DIRS[sDir][1]
    
    # 뒤돌기
    if isOutOfBoard(nx, ny):
      player["dir"] = (player["dir"] + 2) % 4
      nDir = player["dir"]
      nx, ny = sx + DIRS[nDir][0], sy + DIRS[nDir][1]

    player["x"], player["y"] = nx, ny
  

def battle(playerIdx, enemyIdx):
  player = players[playerIdx]
  enemy = players[enemyIdx]
  playerDmg = player["stat"] + player["gun"]
  enemyDmg = enemy["stat"] + enemy["gun"]
  battleRes = [(-playerDmg, -player["stat"], playerIdx), (-enemyDmg, -enemy["stat"], enemyIdx)]
  battleRes.sort()
  # print("BATTLERES: ", battleRes)
  dmgDiff = abs(battleRes[0][0] - battleRes[1][0])
  
  # 승자, 패자, 딜차이
  return [battleRes[0][2], battleRes[1][2], dmgDiff]

def farming(player):
  x, y = player["x"], player["y"]
  # print("FARMING", player)
  fieldGuns = board[y][x]
  if len(fieldGuns) == 0: return
  fieldGuns.sort()
  # 필드건이 더 강하면 교체
  if fieldGuns[-1] > player["gun"]:
    if player["gun"] == 0:
      player["gun"] = fieldGuns[-1]
      fieldGuns.pop()
    else:
      player["gun"], fieldGuns[-1] = fieldGuns[-1], player["gun"]

def dropGun(player):
  global board
  playerGun = player["gun"]
  if playerGun != 0:
    board[player["y"]][player["x"]].append(playerGun)
    player["gun"] = 0

# 자기 방향대로 한 칸 이동
# 만약 다른 플레이어 존재 or 격자 밖
#   오른쪽으로 90도씩 회전하여 빈칸 보이면 순간이동
def moveToEmpty(player):
  # player = players[playerIdx]
  sx, sy = player["x"], player["y"]
  for dirI in range(0, 4):
    nDir = (player["dir"] + dirI) % 4 
    # print("MOVETOEMPTY", nDir, nx, ny)
    nx, ny = sx + DIRS[nDir][0], sy + DIRS[nDir][1]
    if not isOutOfBoard(nx, ny) and getPlayerIdx(nx, ny) == None:
      player["dir"] = nDir
      player["x"], player["y"] = nx, ny
      return
     

for round in range(1, ROUND_CNT + 1):
  for pi in range(1, PLAYER_CNT + 1):  
    # print("ROUND: ", round, "PLAYER: ", pi)
    # 라운드
    # 1.1 1번 플레이어부터 자기 방향 대로 한칸 이동
    #   벽인 경우 반대 방향으로 방향 바꾸고 1 이동
    player = players[pi]
    move(player)
    # 2.1 이동한 방향에 플레이어 없음
    #       총 있음
    #         총 획득
    #         이미 총 가지고 있으면, 더 공격력 높은 총 획득
    #         나머지 총들!은 격자에 둠
    nx, ny = player["x"], player["y"]
    # print("MOVED: ", nx, ny)
    enemyPlayerIdx = getPlayerIdx(nx, ny, pi)
    if enemyPlayerIdx == None:
      farming(player)
    #     이동한 방향에 플레이어 있음
    #       초기 능력치 + 총 공격력 합이 더 큰 플레이어가 이김
    #         같으면 초기 능력치 높은 플레이어 이김 (능력치 같은 경우는 X)
    
    else:
      enemy = players[enemyPlayerIdx]
      winnerIdx, looserIdx, dmgDiff = battle(pi, enemyPlayerIdx)
      # print("BATTLE WIN: ", winnerIdx, " LOOSE: ", looserIdx, " DMG: ", dmgDiff)
      
      #       진 플레이어는 가지고 있는 총 바닥에 내려놓음
      # 자기 방향대로 한 칸 이동
      # 만약 다른 플레이어 존재 or 격자 밖
      #   오른쪽으로 90도씩 회전하여 빈칸 보이면 순간이동
      #         해당 칸에 총 있으면 가장 공격력 높은 총 획득, 나머지 총들은 해당 격자에 내려 놓음
      winner, looser = players[winnerIdx], players[looserIdx]
      dropGun(looser)
      moveToEmpty(looser)
      farming(looser)
      
      # 위 합 계산의 차이 만큼 이긴 플레이어가 점수 획득
      # 이긴 플레이어는 승리칸에 떨어진 총들, 원래 가지고 있던 총들 중 가장 공격력 높은 총 획득, 나머지 총은 드랍
      playerScores[winnerIdx] += dmgDiff
      farming(winner)
   
    # printBoardPlayer()
    # printBoard()
    # printPlyer()
    # print(playerScores)



print(" ".join(map(str, playerScores[1:])))
