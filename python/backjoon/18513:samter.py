# 오답 노트

# heapq에 dict 넣을 때 비교하게 하려고 클래스만드는데 시간 오래잡아먹음...
# 그냥 배열에 넣은담에 인덱스값으로 튜플 만들어서 heapq 넣는게 나을지도

import math
import heapq

MaxPos = 100000000

SCnt, K = map(int, input().split(" "))
SPoss = list(map(int, input().split()))
SPossLen = len(SPoss)
SPoss.sort()

class SNode:
  def __init__(self, dict):
    for k, v in dict.items():
      setattr(self, k, v)
  
  def __lt__(self, other):
    return self.cost <= other.cost
  
  def __str__(self):
    return ', '.join(f"{key}={value}" for key, value in self.__dict__.items())
    
SNodes = []

for i in range(SCnt):
  LSPos, RSPos = -MaxPos * 2, MaxPos * 2
  curPos = SPoss[i]
  if(i >= 1): LSPos = SPoss[i-1]
  if(i < SPossLen-1): RSPos = SPoss[i+1] 
  
  # lMax = curPos - math.ceil(curPos + LSPos)
  # rMax = math.floor(curPos + RSPos) - curPos
  lMax = (curPos - LSPos) // 2
  rMax = (RSPos - curPos) // 2
  if (curPos + RSPos) % 2 == 0: rMax -= 1
  
  
  curSNode = SNode({
    "pos": curPos,
    "lMax": lMax,
    "rMax": rMax,
    "lCnt": 0,
    "rCnt": 0,
    "cost": 1,
  })
  # curCost = curSNode["cost"]
  # print(curSNode["cost"])
  if(lMax == 0 and rMax == 0): continue
  heapq.heappush(SNodes, curSNode)
  
res = 0
# 집 하나씩 짓기
for _ in range(K):
  curSNode = heapq.heappop(SNodes)
  isLFull = curSNode.lMax <= curSNode.lCnt
  isRFull = curSNode.rMax <= curSNode.rCnt
  # 둘 다 max인 경우 -> 다시 안넣는다.
  # print(curSNode)
  if (isLFull and isRFull): continue
  
  curCost = curSNode.cost
  # lr 둘다 max 보다 작은 경우 -> 둘 중에 작은곳에 배치
  if ((not isLFull) and (not isRFull)):
    if (curSNode.lCnt < curSNode.rCnt):
      curSNode.lCnt += 1
      curSNode.cost += 1
    elif (curSNode.lCnt > curSNode.rCnt):
      curSNode.rCnt += 1
      curSNode.cost += 1
    elif (curSNode.lCnt == curSNode.rCnt):
      curSNode.lCnt += 1
  # 둘 중 하나가 max인 경우 -> 다른 한 곳에 배치
  elif (isLFull):
    curSNode.rCnt += 1
    curSNode.cost += 1
  elif (isRFull):
    curSNode.lCnt += 1
    curSNode.cost += 1
  
  
  res += curCost
  isLFull = curSNode.lMax <= curSNode.lCnt
  isRFull = curSNode.rMax <= curSNode.rCnt
  if((not isLFull) or (not isRFull)):
    heapq.heappush(SNodes, curSNode)

    
print(res)
