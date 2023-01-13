# N개행, M개열
N, M = map(int, input().split())
ary = []

for _ in range(0, N):
    ary.append(list(map(int, input().split())))

res = max(map(lambda row: min(row), ary))
print(res)