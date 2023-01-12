# 큰 수의 법칙

N, M, K = map(int, input().split())
array = list(map(int, input().split()))
res = 0
array.sort(reverse=True)
i, j = 0, 0
while i < M:
    if j < K:
        res += array[0]
        j += 1
    else:
        res += array[1]
        j = 0
    i += 1
print(res)



