# 게리맨더링
import math
from collections import deque
from itertools import combinations

MAX_DIFF = 10000000
# 입력
N = int(input())
s_ppl = list(map(int, input().split(' ')))
s_edges = { i:set() for i in range(N)}
for s_num in range(N):
    tmp_in = list(map(lambda x: int(x)-1, input().split()))
    s_edges[s_num] = set(tmp_in[1:])

# print(s_ppl)
# print(s_edges)

# 함수
def is_connected(s_set: set):
    global s_edges
    q = deque()
    vis = set()
    start_s = s_set.pop()
    s_set.add(start_s)
    q.append(start_s)
    vis.add(start_s)
    # print(start_s)
    while q:
        cur_p = q.popleft()
        for to_p in s_edges[cur_p]:
            # print('to_p', cur_p,s_edges[cur_p])
            if to_p not in s_set: continue
            if to_p in vis: continue
            vis.add(to_p)
            q.append(to_p)
    # print(s_set, vis)
    return len(s_set) == len(vis)

def population(s_set: set):
    res = 0
    for s in s_set:
        res += s_ppl[s]
    return res


# 실행
res = MAX_DIFF
union_group = {i for i in range(N)}
for pick_group in range(1, math.floor(N/2) + 1):
    s_idxs = [i for i in range(N)]
    for group1 in combinations(s_idxs, pick_group):
        group1 = set(group1)
        group2 = union_group - group1

        if is_connected(group1) and is_connected(group2):
            diff = abs(population(group1) - population(group2))
            res = min(res, diff)

if res == MAX_DIFF:
    print(-1)
else:
    print(res)
# 나눌 방법 없으면 -1 출력