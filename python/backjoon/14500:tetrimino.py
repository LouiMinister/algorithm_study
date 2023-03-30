# 테트리미노

mis = lambda: map(int, input().split())

# 세로, 가로
N, M = mis()
grid = [list(mis()) for _ in range(N)]
minos = [
    ((0, 0), (0, 1), (0, 2), (0, 3)),
    ((0, 0), (0, 1), (1, 0), (1, 1)),
    ((0, 0), (1, 0), (2, 0), (2, 1)),
    ((0, 1), (1, 1), (2, 1), (2, 0)),
    ((0, 0), (1, 0), (1, 1), (2, 1)),
    ((0, 1), (1, 0), (1, 1), (2, 0)),
    ((0, 0), (0, 1), (0, 2), (1, 1)),
]
mino_turn = [
    [0, 1],
    [0],
    [0, 1, 2, 3],
    [0, 1, 2, 3],
    [0, 1],
    [0, 1],
    [0, 1, 2, 3]
]

def turn_grid(grid):
    h, w = len(grid), len(grid[0])
    next_grid = [[grid[h_i][w_i] for h_i in range(h-1, -1, -1)] for w_i in range(w)]
    return next_grid

# grid 4번 턴 { mino 7개 순회}
score = 0
for turn_cnt in range(4):
    h, w = len(grid), len(grid[0])
    for mino_idx, mino in enumerate(minos):
        if turn_cnt not in mino_turn[mino_idx]: continue
        for d_y in range(h):
            for d_x in range(w):
                cur_mino = [(x+d_x, y+d_y) for x, y in mino if (0 <= x+d_x < w and 0 <= y+d_y < h)]
                if len(cur_mino) < 4: continue
                # if mino_idx == 3:print(cur_mino)
                mino_score = sum(map(lambda xy: grid[xy[1]][xy[0]], cur_mino))
                score = max(score, mino_score)
    grid = turn_grid(grid)
print(score)