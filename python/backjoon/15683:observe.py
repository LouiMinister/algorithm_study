# 감시
from itertools import product

# 1<=N, M <= 8 세로 ,가로
# CCTV 개수 8개

# 시시티비의 개수

# 순열 시시티비의 개수만큼 [0~4, 0~4 ...] -> [0,1,2,3] 에서 중복해서 시시티비 개수만큼 뽑는 순열
# ary = [0,1,2,3]
# perm = product(ary, repeat=4)
# for i in perm:
#     print(i)
FILLED = 99
d_aim = [[0],[0,2],[0,1],[0,1,2],[0,1,2,3]]
d_x = [0, 1, 0, -1]
d_y = [-1, 0, 1, 0]
N, M = map(int, input().split())
field = [list(map(int, input().split())) for i in range(N)]
cam_pos =[]
cam_cnt = 0

for i in range(N):
    for j in range(M):
        if 1 <= field[i][j] <= 5:
            cam_pos.append((j,i,field[i][j]))
            cam_cnt += 1

directions = [0, 1, 2, 3]
cam_directions_candi = product(directions, repeat=cam_cnt)
# 캠의 방향들 set
result = N * M
for cam_directions in cam_directions_candi:
    virtual_field = [row[:] for row in field]
    # 각 캠의 인덱스와 방향
    for cam_idx, cam_direction in enumerate(cam_directions):
        cur_cam_x, cur_cam_y, cur_cam_type = cam_pos[cam_idx]
        # 볼 방향 구하기 위:0, 우:1 하:2 좌:3
        # 현재 보는 방향 + cam_type
        aim = [(cam_direction + d) % 4 for d in d_aim[cur_cam_type-1]]

        for cur_aim in aim:
            d = 0
            while True:
                d += 1
                print(d)
                next_x, next_y = cur_cam_x + d * d_x[cur_aim], cur_cam_y + d * d_y[cur_aim]
                if not (0 <= next_x < M and 0 <= next_y < N): break
                if field[next_y][next_x] == 6: break
                elif 1 <= field[next_y][next_x] <= 5: continue
                elif field[next_y][next_x] == 0:
                    virtual_field[next_y][next_x] = FILLED
    print(*virtual_field, sep='\n')
    empty_cell_cnt = 0
    for i in range(N):
        for j in range(M):
            if virtual_field[i][j] == 0: empty_cell_cnt += 1
    result = min(result, empty_cell_cnt)
print(result)