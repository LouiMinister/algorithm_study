# 2xn 타일링

N = int(input())
DP = [0 for _ in range(N+3)]
DP[0] = 1
DP[1] = 1
DP[2] = 2

def memo(n):
  
  
  for i in range(3, n+1):
    DP[i] = DP[i-2]*2 + DP[i-3]
  return DP[n] % 10007

print(memo(N))
