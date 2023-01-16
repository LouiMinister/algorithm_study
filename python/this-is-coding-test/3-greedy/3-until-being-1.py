# 1이 될 때 까지

in1, in2 = map(int, input().split(' '))

def solution(n, k):
    cnt = 0
    while n != 1:
        cnt += 1
        if n % k == 0:
            n /= k
        else:
            n -= 1
    return cnt

print(solution(in1, in2))