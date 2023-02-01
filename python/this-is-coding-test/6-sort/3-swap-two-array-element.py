n, k = map(int, input().split(' '))
ary1 = list(map(int, input().split(' ')))
ary2 = list(map(int, input().split(' ')))

ary1.sort()
ary2.sort(reverse=True)
for i in range(k):
    if ary1[i] > ary2[i]: break
    ary1[i], ary2[i] = ary2[i], ary1[i]

print(sum(ary1))