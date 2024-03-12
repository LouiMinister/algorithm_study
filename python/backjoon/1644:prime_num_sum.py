# 오답노트

# 아이디어는 어케저케 뽑았는데 투포인터 구현하는데 꽤 오래걸림..
# 걍 투포인터 이동할 때 좌우 이동 어느정도 패딩 두고 로직 돌려도 이상 없으니까 넉넉하게 생각하자!

# 소수의 연속 합
import math

N = int(input())
if (N == 1): 
  print(0)
  exit()
rN = math.floor(N**(1/2))
# print(rN)

primesChk = [True for _ in range(N+1)]

for i in range(2, rN+1):
  for j in range(2, N//i+1):
    # print(i*j)
    primesChk[i*j] = False
    
primes = []
for primeIdx, bool in enumerate(primesChk[2:], start=2):
  if bool: 
    primes.append(primeIdx)
    
res = 0
rangeSum = 0
primesLen = len(primes)
lp, rp = 0, 0

def check(n):
  global res
  # print("check", n)
  if n == N: res += 1

  # 가장 왼쪽에 lp 그 옆에 rp 시작
  
rangeSum += primes[lp]
check(rangeSum)
# if (N in primes): res +=1

# print(primes)
while lp <primesLen:
  # print("LOOP", lp, rp)
  # rangeSum이 N보다 크거나 같아질 때까지 rp 증가
    
  if(rangeSum < N):
    rp += 1
    if rp >= primesLen: break
    rangeSum += primes[rp]
    check(rangeSum)
  if(rangeSum >=N):
    # lp는 1 증가시키고 rp는 1 감소시킴 (rangeSum이 무조건 N보다 작아져야 함)
    rangeSum -= primes[lp]
    lp += 1
    rangeSum -= primes[rp]
    rp -= 1
    check(rangeSum)
      
print(res)
  