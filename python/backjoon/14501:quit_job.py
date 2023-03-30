# 퇴사
# 01:12:48

N = int(input())
T = []
P = []
for i in range(N):
    cur_t, cur_p = map(int, input().split(' '))
    T.append(cur_t)
    P.append(cur_p)

bag = [0] * (N + 1)
for idx in range(N-1, -1, -1):
    candi = []
    if idx + T[idx] <= N:
        candi.append(bag[idx + T[idx]] + P[idx])
    for idx_bw_cur_next in range(idx, idx + T[i] + 1):
        if idx_bw_cur_next < N:
            candi.append(bag[idx_bw_cur_next])
    bag[idx] = max(candi)

print(max(bag))
