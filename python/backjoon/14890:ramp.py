# 경사로

# 길은 총 2N개
# 길에 속한 모든 칸 높이가 같거나 경사로. 경사로 높이는 1 길이는 L
# 경사로는 낮은칸에 놓음. L개의 연속된 칸에 경사로 바닥이 모두 접해야함
# 높이차 1
# 낮은 칸 높이 모두 같아야함. L개 칸 연속
#
# 첫째 줄에 N, L - 둘째 줄 부터 N개의 줄에 지도가 주어짐. 각 칸의 높이는 10보다 작거나 같은 자연수.

N, L = map(int, input().split(' '))
field = []
field_mirror = [[0] * N for _ in range(N)]
for i in range(N):
    field.append(list(map(int, input().split(' '))))
    for j in range(N):
        field_mirror[j][i] = field[i][j]

def check_line(cur_y, field):
    global N, L
    ramp_exist = [False] * N
    for cur_x in range(N - 1):

        if field[cur_y][cur_x] == field[cur_y][cur_x + 1]: continue
        # 한칸 위로 올라가야 하는 경우
        elif field[cur_y][cur_x] + 1 == field[cur_y][cur_x + 1]:
            # L 만큼 뒤로 검색
            for can_x in range(cur_x, cur_x - L, -1):
                if not (0 <= can_x < N): return False
                if ramp_exist[can_x]: return False
                if field[cur_y][cur_x] != field[cur_y][can_x]: return False
            for can_x in range(cur_x, cur_x - L, -1): ramp_exist[can_x] = True
        # 한 칸 내려가야 하는 경우
        elif field[cur_y][cur_x] == field[cur_y][cur_x + 1] + 1:
            for can_x in range(cur_x + 1, cur_x + 1 + L):
                if not (0 <= can_x < N): return False
                if ramp_exist[can_x]: return False
                if field[cur_y][cur_x + 1] != field[cur_y][can_x]: return False
            for can_x in range(cur_x + 1, cur_x + 1 + L): ramp_exist[can_x] = True
        else:
            return False
    return True

result = 0
for cur_y in range(N):
    # print(check_line(cur_y, field))
    if check_line(cur_y, field): result += 1
for cur_x in range(N):
    # print(check_line(cur_x, field_mirror))
    if check_line(cur_x, field_mirror): result +=1
print(result)
