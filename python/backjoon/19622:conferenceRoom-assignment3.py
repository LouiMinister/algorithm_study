# 회의실 배정

N = int(input())
conferences = []
for _ in range(N):
  conferences.append(list(map(int, input().split(" "))))
  
DP = [0 for _ in range(N)]
DP[0] = conferences[0][2]
if(N == 1): 
  print(DP[0])
  exit()
DP[1] = conferences[1][2]

res = max(DP[0], DP[1])
for i in range(2, N):
  DP[i] = max(DP[i-2], DP[i-3]) + conferences[i][2]
  res = max(res, DP[i])


print(res)
