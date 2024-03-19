# 달력

# 일정이 있는 곳에만 코팅지

# 연속된 두 일자 - 각각 일정 1개 이상 = 일정 연속
# 연속된 일정 = 하나의 직사각형에 포함
# 연속된 일정을 모두 감싸는 가장 작은 직사강혁 크기만큼 코팅지 오림

# 일정 = 시작날짜, 종료날짜
# 시작일 순서로 먼저 채워짐
# 같을 경우 긴거 먼저 채워짐
# 가능한 최 상단에 배치
# 하루의 폭은 1

# 1000 * 365 = 365000

N = int(input())

calender = [0 for _ in range(365+2)]

for _ in range(N):
  sd, ed = map(int, input().split(" "))
  for d in range(sd, ed + 1):
    calender[d] += 1
    
    
res = 0
cur_width = 0
cur_height = 0
for d in range(1, 365+2):
  cnt = calender[d]
  if (cnt == 0):
    if cur_width != 0:
      res += cur_width * cur_height
    cur_width, cur_height = 0, 0
  else:
    cur_width += 1
    cur_height = max(cur_height, cnt)
    
print(res)
