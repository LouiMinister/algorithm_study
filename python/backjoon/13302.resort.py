# 오답노트

# 아이디어 떠올리는데 꽤 오래걸림.
# DP인건 알겠고, 날짜를 순회해야 하는 것도 알 것 같은데 쿠폰의 존재 때문에 항상 그 날의 최적값이 Greedy하게 찾아질 수 없다는 생각에 아이디어를 찾지 못함.

# 생각해보니까 현재 가지고 있는 쿠폰수도 DP로 만들면 문제 해결됨.

# DP의 Greedy한 최적값을 구하기 위한 변수를 DP 순회 대상으로 넣자!!



# 하루 이용권 = 10000원
# 3일 이용권 = 25000원 + 쿠폰1 -> 하루당 8300원
  # 쿠폰 쓰는 경우 3.3일 이용권이 25000원 -> 하루당 7575원
# 5일 이용권 
MAX_INT = 10000 * 10000

N, M = map(int, input().split(" "))
MAX_COUPON_CNT = (N // 5) * 3 + 3
block = []
if M > 0:
  block = list(map(int, input().split(" ")))

tickets = [
  {"days": 1, "price": 10000, "coupons": 0},
  {"days": 3, "price": 25000, "coupons": 1},
  {"days": 5, "price": 37000, "coupons": 2},
]

# 날짜, 보유한 쿠폰 수
# 최대 쿠폰 보유 수 40
DP = [[MAX_INT for _ in range(MAX_COUPON_CNT + 1)] for _ in range(N+1)]
DP[0][0] = 0
# print(DP)
for cur_day in range(1, N+1):
  for couponCnt in range(3):
    for ticket in tickets:
      prev_day = cur_day - ticket["days"]
      if prev_day < 0: continue
      
      for prev_couponCnt in range(MAX_COUPON_CNT + 1):
        # 이전 금액이 무한이면 continue
        prev_price = DP[prev_day][prev_couponCnt]
        if prev_price == MAX_INT: continue
        
        cur_coupons, cur_price = None, None
        if cur_day in block and ticket["days"] == 1:
          cur_coupons = prev_couponCnt
          cur_price = prev_price
        elif prev_couponCnt >= 3 and ticket["days"] == 1:
          cur_coupons = prev_couponCnt - 3
          cur_price = prev_price
        else:
          cur_coupons = prev_couponCnt + ticket["coupons"]
          cur_price = prev_price + ticket["price"]
          
        
        DP[cur_day][cur_coupons] = min(cur_price, DP[cur_day][cur_coupons])
        
# for v in DP:
#   print(v)
print(min(DP[N])) 
