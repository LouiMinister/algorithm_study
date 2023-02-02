# 떡볶이 떡 만들기

N, R = map(int, input().split(' '))
ary = list(map(int, input().split(' ')))

left, right = 0, max(ary)

def check(length):
    global ary
    sum = 0
    for ele in ary:
        if ele > length:
            sum += (ele - length)
    return sum


res = 0
while left <= right:
    mid = (left+right)//2
    # print(left, right, mid, check(mid))
    if check(mid) >= R:
        res = mid
        left = mid + 1
    else:
        right = mid - 1
print(res)


