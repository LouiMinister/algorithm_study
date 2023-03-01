# 색종이 모으기(2)

def calc_max(stk_list):
    N = len(stk_list)
    dp = [0] * N
    dp[0] = stk_list[0]
    if len(stk_list) < 2: return dp[0]
    dp[1] = stk_list[1]
    res = max(dp[0], dp[1])

    for x in range(2, N):
        if x > 2:
            dp[x] = stk_list[x] + max(dp[x - 2], dp[x - 3])
        else:
            dp[x] = stk_list[x] + dp[x - 2]
        res = max(res, dp[x])
    return res


def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]

    sticker_1 = sticker[:-1]
    sticker_2 = sticker[1:]

    return max(calc_max(sticker_1), calc_max(sticker_2))