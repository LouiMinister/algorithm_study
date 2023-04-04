# 이차원 배열과 연산

R, C, K = map(int, input().split(' '))
R, C = R-1, C-1
BOUND = 100
grid = [[0] * BOUND for _ in range(BOUND)]
for i in range(3):
    in_row = list(map(int, input().split()))
    for j in range(3):
        grid[i][j] = in_row[j]

def print_grid():
    global grid
    for i in range(BOUND):
        if grid[i][0] == 0: break
        for j in range(BOUND):
            if grid[i][j] == 0: break
            print(grid[i][j], end=' ')
        print('')

width, height = 3, 3
time = 0
while True:
    # print_grid()
    if time > 100:
        print(-1)
        break
    elif grid[R][C] == K:
        print(time)
        break

    time += 1
    width_is_bigger = width > height # 열 정렬
    line_max = 0
    for i in range(width if width_is_bigger else height):
        cate = dict()
        for j in range(height if width_is_bigger else width):
            cur = grid[j][i] if width_is_bigger else grid[i][j]
            if cur == 0: continue
            if cate.get(cur) is None:
                cate[cur] = 0
            cate[cur] += 1
        cate_to_list = list(cate.items())
        cate_to_list.sort(key=lambda tup: (tup[1], tup[0]))
        sorted_list = []
        # 개선 가능
        sorted_list = [v for v in tup for tup in cate_to_list]
        for tup in cate_to_list:
            sorted_list.append(tup[0])
            sorted_list.append(tup[1])
        # formatting
        line_max = max(line_max, len(sorted_list))
        if len(sorted_list) > BOUND:
            sorted_list = sorted_list[0:BOUND]
        else:
            sorted_list = sorted_list + ([0] * (BOUND - len(sorted_list)))
        for j in range(len(sorted_list)):
            if width_is_bigger:
                grid[j][i] = sorted_list[j]
            else:
                grid[i][j] = sorted_list[j]

    if width_is_bigger:
        height = min(line_max, BOUND)
    else:
        width = min(line_max, BOUND)




# print(grid)


# 1 2 999
# 1 2 1
# 2 1 3
# 3 3 3