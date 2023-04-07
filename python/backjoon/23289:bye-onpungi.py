# 온풍기 안녕!
import math
# RxC
# (r,c ) = grid[r][c]
# 모든 칸 0

from collections import deque

# 초기화
def mis(): return map(int, input().split(' '))


dxdy = [(1, 0), (-1, 0), (0, -1), (0, 1)] # 우좌상하
machine = set()  # (x,y,direction)
searching = set() # (x,y)
H, W, K = mis()
input_grid = [list(mis()) for _ in range(H)]
temp_grid = [[0] * W for _ in range(H)]
walls_cnt = int(input())
walls = {tuple(mis()) for _ in range(walls_cnt)}
walls = {(x-1, y-1, d) for x, y, d in walls}

for h_i in range(H):
    for w_i in range(W):
        cur = input_grid[h_i][w_i]
        if 1 <= cur <= 4:
            machine.add((w_i, h_i, cur-1))
        if cur == 5:
            searching.add((w_i, h_i))

# 함수

def in_boundary(x,y):
    global H,W
    return 0 <= x < W and 0 <= y < H

# 항상 직각만 받아야 함
def wall_exist(x1, y1, x2, y2):
    global walls

    if x2 < x1:
        x2, x1 = x1, x2
    if y1 < y2:
        y2, y1 = y1, y2

    if x1 != x2:
        return (y1, x1, 1) in walls
    if y1 != y2:
        return (y1, x1, 0) in walls

def machine_work(m_x, m_y, m_d):
    global W, H, dxdy
    temp_diff_grid = [[0] * W for _ in range(H)]
    # queue에 넣어서 bfs. [(x,y,온도)]
    q = deque()
    d_x, d_y = dxdy[m_d][0], dxdy[m_d][1]
    wind_x, wind_y = m_x + d_x, m_y + d_y
    if not in_boundary(wind_x, wind_y):
        return temp_diff_grid
    temp_diff_grid[wind_y][wind_x] = 5
    q.append((wind_x, wind_y, 5)) # x, y, 온도
    while q:
        cur_x, cur_y, cur_t = q.popleft()
        if cur_t <= 1: continue
        # 대각
        ddxy = None
        if m_d < 2: ddxy = [(0, 1),(0, -1)]
        else: ddxy = [(1, 0), (-1, 0)]
        for dd_x, dd_y in ddxy:
            next_x, next_y = cur_x + dd_x, cur_y + dd_y
            if not in_boundary(next_x, next_y): continue
            next_next_x, next_next_y = next_x + d_x, next_y + d_y
            if not in_boundary(next_next_x, next_next_y): continue
            if (not wall_exist(cur_x, cur_y, next_x, next_y)) and (not wall_exist(next_x, next_y, next_next_x, next_next_y)):
                temp_diff_grid[next_next_y][next_next_x] = cur_t - 1
                q.append((next_next_x, next_next_y, cur_t - 1))
        # 직각
        next_x, next_y = cur_x + d_x, cur_y + d_y
        if not in_boundary(next_x, next_y): continue
        if not wall_exist(cur_x, cur_y, next_x, next_y):
            temp_diff_grid[next_y][next_x] = cur_t - 1
            q.append((next_x, next_y, cur_t - 1))
    return temp_diff_grid


# 온풍기의 온도상승은 각각의 합이다.
# 온풍기의 온도가 퍼질 때 각 레이어는 일정하다
# 온풍기의 위치도 온도 상승이 가능하다.
# 바람 만드는 함수
    # 한 칸에 온도가 k만큼 상승하면 , 그 다음 방사형으로 k-1만큼 상승
    # set 이용
def run():
    global H, W, machine, temp_grid
    for m_x, m_y, m_d in machine:
        cur_temp_diff_grid = machine_work(m_x,m_y,m_d)
        # print('cur-temp-diff')
        # print(*cur_temp_diff_grid, sep='\n')
        for i in range(H):
            for j in range(W):
                temp_grid[i][j] += cur_temp_diff_grid[i][j]



# 높은 칸에서 낮은 칸으로 두 칸 온도차 / 4 내림 만큼 온도 조절됨
# 사방으로 퍼짐
# 벽있으면 안가짐
# 온도 조절하는 함수
    # 온도 조절된만큼 원래칸 감소
    # 모든 칸 동시에 발생 - 배열에 증감 담아놨다가 한번에 처리
def exp():
    global temp_grid, W, H
    temp_diff_grid = [[0] * W for _ in range(H)]
    for cur_y in range(H):
        for cur_x in range(W):
            cur_temp = temp_grid[cur_y][cur_x]
            for dx, dy in [(1, 0), (0, 1)]:
                next_x, next_y = cur_x + dx, cur_y + dy
                if not in_boundary(next_x, next_y): continue
                if wall_exist(cur_x, cur_y, next_x, next_y):
                    continue
                next_temp = temp_grid[next_y][next_x]
                if cur_temp < next_temp:
                    diff_temp = math.floor((next_temp - cur_temp)/4)
                    temp_diff_grid[next_y][next_x] -= diff_temp
                    temp_diff_grid[cur_y][cur_x] += diff_temp
                if next_temp < cur_temp:
                    diff_temp = math.floor((cur_temp - next_temp) / 4)
                    temp_diff_grid[cur_y][cur_x] -= diff_temp
                    temp_diff_grid[next_y][next_x] += diff_temp
    for i in range(H):
        for j in range(W):
            temp_grid[i][j] += temp_diff_grid[i][j]

# 가장 바깥쪽 온도 1감소
def dec():
    global W, H, temp_grid
    for i in range(0, W): # x 0 ~ W-1
        for j in [0, H-1]: # y 0, H-1
            temp_grid[j][i] = max(temp_grid[j][i] - 1, 0)
    for i in range(1, H-1): # y 1 ~ H-2
        for j in [0, W-1]: # x 0, W-1
            temp_grid[i][j] = max(temp_grid[i][j] - 1, 0)




# 서치 - 조사하는 모든 칸 온도가 K 이상인지 확인
def check():
    global searching, K
    for x, y in searching:
        if temp_grid[y][x] < K:
            return False
    return True

# 실행
chocolate = 0
while True:
    # 모든 온풍기에서 바람
    run()
    # 온도 조절
    exp()
    # 온도가 1 이상인 가장 바깥쪽 칸 온도 1씩 감소
    dec()
    # 초콜릿 먹기
    chocolate += 1
    # 조사하는 모든 칸 온도가 K 이상인지 검사 - 해당하면 종료, 아니면 반복
    if check():
        print(chocolate)
        break
    if chocolate > 100: ###############################################################################################100
        print(101)
        break
