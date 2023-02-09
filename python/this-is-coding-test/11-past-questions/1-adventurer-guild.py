# 모험가 길드

N = int(input())
ary = list(map(int, input().split(' ')))
ary.sort()
goal = 0
cnt = 0
res = 0

for val in ary:
    cnt += 1
    goal = val
    if cnt >= goal:
        res += 1
        cnt = 0

print(res)