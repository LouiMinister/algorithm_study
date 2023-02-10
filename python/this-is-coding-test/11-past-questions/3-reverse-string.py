# 문자열 뒤집기

cnt = [0, 0]

ary = list(map(int, input()))

prev = ary[0]
cnt[ary[0]] += 1

for ele in ary[1:]:
    if prev is not ele:
        prev = ele
        cnt[ele] += 1

print(min(cnt))