import sys
N, K = list(map(int, sys.stdin.readline().rstrip().split()))
Cost, Weight = [0], [0]
WMax = 0
for i in range(N):
    in1, in2 = list(map(int, sys.stdin.readline().rstrip().split()))
    Weight.append(in1)
    Cost.append(in2)
DP = [[0 for col in range(N+1)] for row in range(K+1)]
for weightI in range(1, K+1):
    for itemI in range(1, N+1):
        candi = [DP[weightI][itemI - 1], DP[weightI-1][itemI]]
        if weightI-Weight[itemI] >= 0:
            candi.append(DP[weightI-Weight[itemI]][itemI-1] + Cost[itemI])
        DP[weightI][itemI] = max(candi)
print(max(DP[K]))