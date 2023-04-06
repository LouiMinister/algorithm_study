# 마법사 상워아 비바라기
def mis(): return map(int, input().split(' '))

# 초기화
e_dxdy = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
f_dxdy = [(-1, -1), (1, -1), (1, 1), (-1, 1)]
W, C = mis()
grid = [list(mis()) for _ in range(W)]
arrow, dist = [0] * C, [0] * C
for i in range(C):
    arrow[i], dist[i] = mis()

clouds = {(0, W-1), (1, W-1), (0, W-2), (1, W-2)}

# 함수
def move(direction, distance):
    global clouds, W, e_dxdy
    moved_cloud = set()
    dx, dy = e_dxdy[direction][0] * distance, e_dxdy[direction][1] * distance
    for cloud_x, cloud_y in clouds:
        next_x, next_y = (cloud_x + dx + W) % W, (cloud_y + dy + W) % W
        moved_cloud.add((next_x, next_y))
    clouds = moved_cloud

def diag_pos(x,y):
    global f_dxdy, W
    for dx, dy in f_dxdy:
        n_x, n_y = x + dx, y + dy
        if 0 <= n_x < W and 0 <= n_y < W:
            yield n_x, n_y


# 실행
for i in range(C):
    # 구름이 arrow 방향으로 dist 만큼 이동
    direction, distance = arrow[i], dist[i]
    move(direction - 1, distance)

    # 각 구름에서 비내리기 - 칸에 물 양 + 1
    for cloud_x, cloud_y in clouds:
        grid[cloud_y][cloud_x] += 1
    # 구름 사라지기

    # 물이 증가한 칸 (r,c)에 물복사 버그
        # 물이 있는 대각선으로 인접한 바구니 수 많큼 (r,c) 바구니 물 증가 (경계선 넘어서는 아님)
        # 한번에 반영되도록
        # 물이 증가한 칸 = 구름이 있던 칸
            # 비 내리자마자 대각 비교하고 water_copy 집합에 append
    grid_water_plus = set()
    for cloud_x, cloud_y in clouds:
        diag_water_cnt = 0
        for diag_x, diag_y in diag_pos(cloud_x, cloud_y):
            if grid[diag_y][diag_x] > 0:
                diag_water_cnt += 1
        if diag_water_cnt >= 1:
            grid_water_plus.add((cloud_x, cloud_y, diag_water_cnt))
    for x, y, cnt in grid_water_plus:
        grid[y][x] += cnt

    # 바구니 물 2 이상인 모든 칸에 구름 생기고 물 -2. (3에서 구름이 사라진 칸이면 X)
        # 전체 탐색
        # 현재 구름 집합 = 새로 생긴 구름 집합 - 현재 구름 집합
    new_clouds = set()
    for c_y in range(W):
        for c_x in range(W):
            if grid[c_y][c_x] >= 2 and (c_x, c_y) not in clouds:
                grid[c_y][c_x] -= 2
                new_clouds.add((c_x, c_y))
    clouds = new_clouds
# 결과
    # 물의 합 총합
res = 0
for i in range(W):
    for j in range(W):
        res += grid[i][j]
print(res)
