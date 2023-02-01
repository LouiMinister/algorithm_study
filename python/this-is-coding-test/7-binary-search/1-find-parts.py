# 부품 찾기
import sys

def b_search(ary, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if ary[mid] == target:
            return True
        elif target < ary[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return False


n1 = int(input())
ary1 = list(map(int, sys.stdin.readline().rstrip().split(' ')))
ary1.sort()
n2 = int(input())
ary2 = list(map(int, sys.stdin.readline().rstrip().split(' ')))

for i in range(n2):
    if b_search(ary1, ary2[i], 0, len(ary1)-1):
        print('yes', end=' ')
    else:
        print('no', end=' ')