# 국영수

N = int(input())
score = []
for i in range(N):
    score.append(list(input().split(' ')))
    for j in range(1,4):
        score[i][j] = int(score[i][j])
print(score)
score.sort(key=lambda s:(-s[1], s[2], -s[3], s[0]))
for s in score:
    print(s[0])

# 12
# Junkyu 50 60 100
# Sang 80 60 50
# suny 80 70 100
# soo 50 60 90
# hae 50 60 100
# kang 60 80 100
# dong 80 60 100
# sei 70 70 70
# won 70 70 90
# san 70 70 80
# nsj 80 80 80
# tae 50 60 90