# 등굣길

def solution(m, n, puddles):
    field = [[0] * (m + 1) for _ in range(n + 1)]
    field[1][1] = 1
    for x, y in puddles:
        field[y][x] = 'p'

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1: continue
            if field[i][j] == 'p': continue
            # print(j,i)
            cur = 0
            if field[i][j - 1] != 'p':
                cur += field[i][j - 1]
            if field[i - 1][j] != 'p':
                cur += field[i - 1][j]
            field[i][j] = cur % 1000000007
    print(field)
    return field[n][m]