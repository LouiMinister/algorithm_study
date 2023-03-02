#인구 이동

# 1<=N<=50, 1<=L<=R<=100
# NxN
# 각각 땅에 인구
# L 명 이상 R명 이하 -> 국경선 염
# 연합 인구수 / 칸 수

# 국경선 한번도 안열렸으면 끝
# N N 순회
# 국경선 열리는지 체크
# 한 점에서 dfs -> vis 표시, sum 누적, 이동한 곳 메모
from collections import deque

# 3 5 10
# 10 15 20
# 20 30 25
# 40 22 10

N, L, R = map(int, input().split(' '))
field = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
for _ in range(N):
    field.append(list(map(int, input().split(' '))))

vis_per_move = []


# vis_on_step = []
# union_trace = []
# union_ppl = 0
# def clear():
#     global union_trace, union_ppl
#     union_trace = []
#     union_ppl = 0
#
# def dfs(x, y):
#     global L, R, vis_on_step, union_ppl, union_trace
#     print('dfs!')
#     stack = deque()
#     stack.append((x, y))
#     while stack:
#         print(stack)
#         xx, yy = stack.pop()
#         if vis_on_step[yy][xx]: return
#         vis_on_step[yy][xx] = True
#         union_ppl += field[yy][xx]
#         union_trace.append((xx, yy))
#         for d in range(4):
#             nx, ny = xx + dx[d], yy + dy[d]
#             if not (0 <= nx < N and 0 <= ny < N): continue
#             print(field[yy][xx], field[ny][nx])
#             if field[ny][nx] is True: continue
#             if L <= abs(field[ny][nx] - field[yy][xx]) <= R:
#                 print((nx,ny))
#                 stack.append((nx, ny))
#
# def distribute():
#     global field, union_trace, union_ppl
#     print(field)
#     print(union_trace)
#     for x, y in union_trace:
#         field[y][x] = union_ppl // len(union_trace)
#
#
# res = 0
# opened = False
# while True:
#     vis_on_step = [[False] * N for _ in range(N)]
#     opened = False
#     for i in range(N):
#         for j in range(N):
#             clear()
#             if vis_on_step[i][j] is True: continue
#             dfs(j, i)
#             if len(union_trace) >= 2:
#                 distribute()
#                 opened = True
#     if opened:
#         res += 1
#     else:
#         break
#
# print(res)
#
# # [20, 20, 20]
# # [20, 20, 20]
# # [40, 20, 10]