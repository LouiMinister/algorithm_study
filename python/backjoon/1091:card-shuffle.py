# # 카드 섞기

# 3 명의 플레이어
# N 개의 카드

# 각 카드: 카드idx % 3 플레이어

# 방법: 길이가 N인 수열 S. -> i번째 위치에 있던 카드는 S[i]로 이동
# 48>=N>=3 3의 배수
# 원소는 모두 N-1 보다 작거나 같은 자연수 또는 0, 중복 X

# 목표: 길이가 N인 수열 P -> i 번째 위체 있는 카드를 플레이어 P[i]에게 보내야 함
# 수는 0, 1, 2, 중 하나

# 안되면 -1 출력

# 3
# 2 0 1
# S = 1 2 0

# 원래 카드는 0, 1, 2 
# ->  2, 0, 1
# ->  1 2 0
# ==  0 -> 1로, 1은 2로, 2는 0으로

import copy

N = int(input())
P = list(map(int, input().split(" ")))
S = list(map(int, input().split(" ")))

originCards = [i for i in range(N)]
cards = copy.deepcopy(originCards)

def achieve(cards):
  global P
  # for i, player in P:
  #   cards의 카드 card(i)의 index % 3 == P[i] 이어야 함
  
  for cardIdx, card in enumerate(cards):
    playerNum = cardIdx % 3
    if P[card] != playerNum: return False
  return True
     

def shuffle(cards):
  global S, N
  newCards = [0 for _ in range(N)]
  for idx, toIdx in enumerate(S):
    card = cards[idx]
    newCards[toIdx] = card
  return newCards

LOOP_MAX = 10000000
res = 0

if achieve(cards):
  print(0)
  exit()
  
while(res < LOOP_MAX):
  res += 1
  cards = shuffle(cards)
  if achieve(cards): break
  if cards == originCards:
    res = -1
    break
  
if res == LOOP_MAX:
  print(-1)
else:
  print(res)
