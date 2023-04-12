# 세 용액

# 3 <= N <= 5000
# 완탐 - 20833333333 >= 200억 -> 불가능
# 5000 * 5000 = 25 000 000 > 2천5백만
# 투포인터 하고 가운데 낑겨서 돌리게 하기  -> 5000 * 25000
# -> 투 포인터 + 이분 탐색

N = int(input())
slts = list(map(int,input().split(' ')))
slts.sort()
min_abs_sum = 3123123123
res = []

def idx_sum(idx1, idx2, idx3):
    global slts
    return abs(slts[idx1] + slts[idx2] + slts[idx3])


for m_idx in range(1, N-1):
    l_idx, r_idx = 0, N - 1
    while True:
        if idx_sum(l_idx, m_idx, r_idx) < min_abs_sum:
            min_abs_sum = idx_sum(l_idx, m_idx, r_idx)
            res = [slts[l_idx], slts[m_idx], slts[r_idx]]
        if m_idx - 1 == l_idx and m_idx + 1 == r_idx: break
        if m_idx - 1 == l_idx:
            r_idx -= 1
            continue
        if m_idx + 1 == r_idx:
            l_idx += 1
            continue
        if idx_sum(l_idx + 1, m_idx, r_idx) < idx_sum(l_idx, m_idx, r_idx - 1):
            l_idx += 1
        else:
            r_idx -= 1

print(*res)

# ll_idx, rr_idx = 0, N-1
# while ll_idx + 1 < rr_idx:
#     pre_res = slts[ll_idx] + slts[rr_idx]
#     # 양 끝 구간 l_idx, r_idx 도 후보군에 포함되어야 한다.
#     l_idx = ll_idx + 1
#     r_idx = rr_idx - 1
#     while True:
#         m_idx = (l_idx + r_idx) / 2
#         # mid랑 mid 좌, mid 우 비교해서 구간 재조정
#         m_res = abs(pre_res + slts[m_idx])
#         # mid 보다 왼쪽이 더 작으면 오른쪽 범위 감소
#         if l_idx <= m_idx - 1 and abs(pre_res + slts[m_idx - 1]) < m_res:
#             r_idx = m_idx - 1
#         # mid 보다 오른족이 더 작으면 왼쪽 범위 감소
#         elif m_idx + 1 <= r_idx and abs(pre_res + slts[m_idx + 1]) < m_res:
#             l_idx = m_idx + 1
#         # 둘다 아니면 mid 가 최적화된 답임
#         else:
#             if m_res < min_abs_sum:
#                 min_abs_sum = m_res
#                 res = [slts[ll_idx], slts[m_idx] slts[rr_idx]]
#             break









