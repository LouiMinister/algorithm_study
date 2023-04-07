from itertools import permutations
import copy

# 입력
# 3~50, 1~6
H, W, op_cnt = map(int, input().split(' '))
grid = [list(map(int, input().split(' '))) for _ in range(H)]
grid_origin = copy.deepcopy(grid)
ops = [list(map(int, input().split(' '))) for _ in range(op_cnt)]

# 배열값 = 행합의 최솟값
def ary_value():
    global grid
    return min(*[sum(grid[h_i]) for h_i in range(H)])



# 회전연산 (y, x, s) -> (y-s, x-s), (y+s, x+s) 를 시계 방향으로 한칸씩
def ary_spin(x, y, s):
    global grid
    for i in range(1, s+1):
        corner = grid[y-i][x-i]
        for dy in range(y-i, y+i, 1):
            grid[dy][x-i] = grid[dy+1][x-i]
        for dx in range(x-i, x+i, 1):
            grid[y+i][dx] = grid[y+i][dx+1]
        for dy in range(y+i, y-i, -1):
            grid[dy][x+i] = grid[dy-1][x+i]
        for dx in range(x+i, x-i, -1):
            grid[y-i][dx] = grid[y-i][dx-1]
        grid[y-i][x-i+1] = corner


# 실행
idx_cnd = list(range(op_cnt))
idx_pmt = permutations(idx_cnd)

res = 100 * 50
for op_order in idx_pmt:
    grid = copy.deepcopy(grid_origin)
    for op_idx in op_order:
        y, x, s = ops[op_idx]
        ary_spin(x-1, y-1, s)
    res = min(res, ary_value())
print(res)


