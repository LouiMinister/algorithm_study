# 오답노트

# 일반적인 방법으로 하면 시간 초과 하고, 우선순위 큐를 사용해야 겠다는 아이디어 까지는 떠올림
# 근데 중앙값을 내려고 하니 우선순위 큐를 더 어떻게 확장할 생각을 못함.
# 우선순위큐 두개를 이용해서 중앙 값을 만들 생각을 못함.

# 그리고 최대 힙 만드는걸 까먹음. 이후에 그냥 -인자 넣는 식으로 했는데 일케하니까 개헷갈림... 담엔 추상화해서 하자(튜플로 우선순위 정하기)

# N인 경우 -> 10000000 천만
import heapq
from functools import cmp_to_key

MAX_INT, MIN_INT = 2**33, -2**33

TC = int(input())

def deflate(minPq, maxPq):
  diff = len(minPq) - len(maxPq)
  if diff >= 2:
    for _ in range(diff//2):
      heapq.heappush(maxPq,-heapq.heappop(minPq))
  if diff <= -2:
    for _ in range((-diff)//2):
      heapq.heappush(minPq,-heapq.heappop(maxPq))  

def mid(ary):
  answer = [ary[0]]
  if (len(ary) == 1): return answer
  max_pq = []
  min_pq = []
  if(ary[0] > ary[1]):
    max_pq.append(-ary[1])
    min_pq.append(ary[0])
  else:
    min_pq.append(ary[1])
    max_pq.append(-ary[0])
  
  for i, v in enumerate(ary[2:]):
    if (len(max_pq) == 0):
      heapq.heappush(max_pq, -v)
    elif (len(min_pq) == 0):
      heapq.heappush(min_pq, v)
    elif (v > min_pq[0]):
      heapq.heappush(min_pq, v)
    elif (v < -max_pq[0]):
      heapq.heappush(max_pq, -v)
    else:
      heapq.heappush(min_pq, v)
    
    # print(v)
    # print(max_pq)
    # print(min_pq)
    # print("--------------------------")
    if(i%2 == 0): # 짝수면
      deflate(min_pq, max_pq)
      if(len(min_pq) > len(max_pq)):
        answer.append(min_pq[0])
      else:
        answer.append(-max_pq[0])
  
  return answer
    

for _ in range(TC):
  N = int(input())
  ary = []
  loopCnt = (N-1)//10 + 1
  for _ in range(loopCnt):
    ary.extend(list(map(int, input().split(" "))))
  answer = mid(ary)
  
  answer_len = len(answer)
  loopCnt = (answer_len-1)//10 + 1
  print(answer_len)
  for i in range(loopCnt):
    if(i == loopCnt -1):
      print(" ".join(map(str, answer[i*10:])))
    else:
      print(" ".join(map(str, answer[i*10:(i+1)*10])))
  
  
# print(MAX_INT, MIN_INT)
