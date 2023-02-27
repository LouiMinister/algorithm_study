# 삼각 달팽이

def solution(n):
    field = [[None] * n for _ in range(n)]
    circle_cnt = (n - 1) // 3 + 1

    x, y = 0, 0
    num = 1
    for i in range(circle_cnt):
        if n - 1 - i * 3 == 0:
            field[y][x] = num
        for j in range(n - 1 - i * 3):
            field[y][x] = num
            num += 1
            y += 1
        for j in range(n - 1 - i * 3):
            field[y][x] = num
            num += 1
            x += 1
        for j in range(n - 1 - i * 3):
            field[y][x] = num
            num += 1
            x -= 1
            y -= 1
        x += 1
        y += 2
    result = sum(list(map(lambda ary: list(filter(lambda ele: ele != None, ary)), field)), [])
    return result