# 만들 수 없는 금액

N = int(input())
coins = list(map(int, input().split(' ')))
coins.sort()

can_make = 0
res = 0
for coin in coins:
    if can_make + 1 >= coin:
        can_make = can_make + coin
    else:
        print(can_make + 1)
        break
if can_make == sum(coins):
    print(can_make + 1)