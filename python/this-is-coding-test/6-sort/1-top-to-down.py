# 위에서 아래로
n = int(input())
ary = []
for i in range(n):
    ary.append(int(input()))

ary.sort(reverse=True)
for i in ary:
    print(i, end=' ')