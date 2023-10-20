import sys

N, M = list(map(int, sys.stdin.readline().split()))
trees = list(map(int, sys.stdin.readline().split()))
# N, M = 4, 7
# trees = [20, 15, 10, 17]

def check(cutHeight):
    global M, trees
    res = 0
    for tree in trees:
        if tree > cutHeight:
            res += tree - cutHeight
    return res >= M

left, right = 1, 2000000000
ans = 0
while left <= right:
    mid = (left + right)//2
    # print(f"{left} {mid} {right}")
    if check(mid):
        ans = mid
        left = mid+1
    else:
        right = mid-1
print(ans)
