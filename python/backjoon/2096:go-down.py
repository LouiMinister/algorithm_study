# n = int(input())
# area = []
# for i in range(1, n+1):
#     area.append(list(map(int, input().split())))

# minV = 1123456
# maxV = 0

# def dfs(x, y, res):
#     global minV, maxV
#     if y == n-1:
#         minV = min(minV, res)
#         maxV = max(maxV, res)
#     else:
#         for i in range(-1, 2):
#             nx = x + i
#             if 0 <= nx <= 2 and y <= n:
#                 dfs(nx, y+1, res+area[y+1][nx])

# dfs(1, -1, 0)
# print(f"{maxV} {minV}")

import copy

n = int(input())
data = [list(map(int, input().split())), []]
minRes = [copy.deepcopy(data[0]), [1123456, 1123456, 1123456]]
maxRes = [copy.deepcopy(data[0]), [0, 0, 0]]

for i in range(1, n):
    print
    curI = i % 2
    nextI = (i+1) % 2
    data[curI] = list(map(int, input().split()))
    for x in range(3):
        for dx in range(-1, 2):
            nx = x + dx
            if nx < 0 or nx > 2:
                continue
            minRes[curI][nx] = min(
                minRes[curI][nx], minRes[nextI][x] + data[curI][nx])
            maxRes[curI][nx] = max(
                maxRes[curI][nx], maxRes[nextI][x] + data[curI][nx])
    minRes[nextI] = [1123456, 1123456, 1123456]

print(f"{max(maxRes[(n+1)%2])} {min(minRes[(n+1)%2])}")
