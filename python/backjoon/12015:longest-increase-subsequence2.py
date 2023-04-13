# 가장 긴 증가하는 부분수율 2

N = int(input())
ary = list(map(int,input().split()))

dp = [ary[0]]

def update(e):
    global dp
    if dp[len(dp)-1] < e:
        dp.append(e)
    else:
        l_i, r_i = 0, len(dp) - 1
        while l_i <= r_i:
            if l_i == r_i:
                dp[l_i] = e
                return
            m_i = (l_i + r_i)//2
            if  e <= dp[m_i]:
                r_i = m_i
            else:
                l_i = m_i + 1


for e in ary[1:]:
    update(e)
print(len(dp))