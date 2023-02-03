# 개미 전사

N = int(input())
ary = list(map(int, input().split(' ')))

memo = [None] * N
memo[0] = ary[0]


def dp(n):
    global ary, memo
    if n < 0:
        return 0
    if memo[n] is None:

        memo[n] = max(dp(n - 2) + ary[n], dp(n - 1))
        print(memo)
    return memo[n]


print(dp(N-1))
