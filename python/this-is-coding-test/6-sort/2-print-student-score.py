# 성적이 낮은 순서로 학생 출력하기

n = int(input())
ary = []
for i in range(n):
    inputs = input().split(' ')
    ary.append((inputs[0], int(inputs[1])))

ary.sort(key = lambda ele: ele[1])
for i in ary:
    print(i[0], end=' ')