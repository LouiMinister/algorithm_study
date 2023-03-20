# 로봇 청소기
# x, y 순서 반대로 받아서 시간 엄청씀... 지문 다 꼼꼼히 읽자

# N, M 직사각형, 방향 N-1, M-1
# 1. 청소
# 2. 4칸 청소되지 않은 곳 없으면 한칸 후진. 후진할곳 벽이면 작동중지
# 3. 청소 되자 않은 곳 있으면 반시계 회전. 앞에 빈칸이면 전진 반복
#
# d 북 동 남 서 0 1 2 3
# 0 - 청소되지 않은 칸
# 1 - 벽이 있음
# 2 - 청소된칸


dx = [0, 1, 0, -1]
dy = [-1, 0 ,1, 0]
N, M = map(int, input().split(' '))
cur_y, cur_x, cur_d = map(int, input().split(' '))
field = []
res = 0

for i in range(N):
    field.append(list(map(int, input().split(' '))))

def all_cleand(x, y):
    global field, dx, dy
    for i in range(4):
        if field[y + dy[i]][x + dx[i]] == 0:
            return False
    return True


while True:
    # print(cur_x, cur_y, cur_d)
    # 1. 청소
    if field[cur_y][cur_x] == 0:
        field[cur_y][cur_x] = 2
        res += 1
    # 2. 4칸 청소되지 않은 곳 없으면 한칸 후진. 후진할곳 벽이면 작동중지
    elif all_cleand(cur_x, cur_y):
        back_d = (cur_d + 2) % 4
        next_x, next_y = cur_x + dx[back_d], cur_y + dy[back_d]

        if field[next_y][next_x] == 1:
            break
        else:
            cur_x, cur_y = next_x, next_y
    else:
        cur_d = (cur_d + 3) % 4
        next_x, next_y = cur_x + dx[cur_d], cur_y + dy[cur_d]
        if field[next_y][next_x] == 0:
            cur_x, cur_y = next_x, next_y
    # 3. 청소 되자 않은 곳 있으면 반시계 회전. 앞에 빈칸이면 전진 반복

print(res)