

# N 일동안 맥주 축제
# K 종류의 맥주

# N일간 맥주 N병

# 맥주별 - 선호도, 도수 레벨
# 도수 레벨 > 간 레벨 -> 맥주병

# 맥주 N개의 합이 M 이상이 되도록 함
# 간 레벨의 최솟값 구하기
# K 개중 N개의 맥주를 고른다 -> 
# 고른 맥주들의 합이 선호보다 큰지 확인한다
# -> 시간 초과

# 백팩문제같은데

# 1 4
# 2 5
# 3 3
# 4 3
# 4 6


# 간 레벨로 이분탐색인가
# 간 레벨이 3이면 3이하의 도수를 가진 술 내림차순 정렬해서 위에서부터 N개 골라서 합이 선호도다 이상이 되도록 해야한다.

# N <= 200,000   M < 2^31, K <= 200,000
N, M, K = map(int, input().split(' ')) # 날, 선호도합, 맥주종류

# 아무리 레벨 올려도 조건 만족 못하면 -1 출력후 끝

# [만족도, 도수] -> 선호도 내림차순, 도수 내림차순
maxDosu = 0
beers = []
for _ in range(K):
  favor, dosu =  map(int, input().split(' '))
  maxDosu = max(maxDosu, dosu)
  beers.append([favor,dosu])
beers.sort(key = lambda beer: (-beer[0], -beer[1]))

def check(lv):
  leftBeersCnt = N
  favorSum = 0
  for favor, dosu in beers:
    if leftBeersCnt <= 0: break
    if lv >= dosu:
      favorSum += favor
      leftBeersCnt -= 1
  return favorSum >= M and leftBeersCnt <=0

# print(beers)

answer = -1
l, r = 0, maxDosu
mid = 0
while (l <= r):
  mid = (l+r)//2
  if(check(mid)):
    answer = mid
    r = mid -1
  else:
    l = mid + 1
  
print(answer)
