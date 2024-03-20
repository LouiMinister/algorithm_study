# 동전 게임

# 비트마스킹

# 뒤집는 경우가 8가지를 각각 할지 말지 고르는거라 00000000 ~ 11111111 경우 즉 512 가지수이다. 이걸 생각 이상하게함
# bfs로 모든 경우 bruteforce 해도 되긴 하는데 그냥 그 숫자만큼 돌려도 될 거 같긴 함.

from collections import deque

TC = int(input())

def coinToInt(char):
  if char == "H": return "1"
  elif char == "T": return "0"

def flip(coinBinary, cmd):
  if(cmd < 3): # 수평
    return coinBinary ^ (0b111 << (cmd % 3)*3)
  elif(cmd < 6): # 수직
    return coinBinary ^ (0b1001001 << (cmd % 3))
  elif(cmd == 6): # 아랫대각
    return coinBinary ^ 0b100010001
  elif(cmd == 7): # 윗대각
    return coinBinary ^ 0b001010100
  
def isAllSameCoins(coinBinary):
  return (coinBinary == 0b000000000 or coinBinary == 0b111111111)
  
def bfs(coinBinary):
  res = 10
  # 큐에 (코인값, cmd단계, 뒤집은 횟수)
  dq = deque()
  dq.append((coinBinary, 0, 0))
  
  while dq:
    curCoin, cmdLev, flipCnt = dq.popleft()
    
    if (isAllSameCoins(curCoin)): res = min(res, flipCnt)
    if (cmdLev > 7): continue
    
    # cmd 안하고 바로 넣는 경우
    dq.append((curCoin, cmdLev+1, flipCnt))
    
    # cmd 하고 넣는 경우
    nextCoin = flip(curCoin, cmdLev)
    dq.append((nextCoin, cmdLev+1, flipCnt+1))
  
  if res == 10: return -1
  else: return res

for _ in range(TC):
  coinAry = []
  # 입력 받아서 000000000 ~ 111111111 이진수로 만들기 (H=1, T=0)
  for _ in range(3):
    coinAry.extend(map(coinToInt, input().split(" ")))
  coinBinaryStr = "".join(coinAry)
  coinBinary = int(coinBinaryStr, 2)
  # print(coinBinary)
  print(bfs(coinBinary))

  # 뒤집기 함수(코인이진수, 번호 0~7)


  # 뒤집기 bfs
    # 수평 3개 뒤집기, 수직 3개 뒤집기, 대각 2개 뒤집기 를 bfs로 순회 (2^8)
    # 만약 뒤집어서 000000000 이 되거나 111111111 이 되면 통과, 결과값 반환  


# dec = 291
# binary = format(dec, "b")
# print(binary)


# afterBinary = flip(dec, 4)
# print(format(afterBinary, "b"))

# # 010 010 
