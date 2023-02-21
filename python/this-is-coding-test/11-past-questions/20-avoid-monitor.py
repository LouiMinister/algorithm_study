# 감시 피하기
from itertools import combinations

N = int(input())
field = []
teachers = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
for i in range(N):
    row = list(input().split(' '))
    field.append(row)
    for j in range(N):
        if field[i][j] == 'T':
            teachers.append((i, j))

def discovered():
    global field, teachers, dx, dy
    for ty, tx in teachers:
        for d in range(4):
            for m in range(1, N):
                ny = ty + dy[d] * m
                nx = tx + dx[d] * m
                if (not (0 <= nx < N and 0 <= ny < N)) or field[ny][nx] == 'O': break
                if field[ny][nx] == 'S':
                    return True
    return False

def solution():
    global N, field
    candi = []
    for i in range(N):
        for j in range(N):
            if field[i][j] == 'X':
                candi.append((i, j))
    combs = combinations(candi, 3)

    for comb in combs:
        for y, x in comb:
            field[y][x] = 'O'
        if not discovered():
            print('YES')
            return
        for y, x in comb:
            field[y][x] = 'X'
    print('NO')


solution()