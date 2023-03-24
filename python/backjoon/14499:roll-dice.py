# N M 지도. r은 북에서 떨어진 칸 개수, c는 에서 떨어진 칸 개수
#
# 이동한 칸 = 0 -> 주사위 바닥면이 칸에 복사
# 아니면 -> 칸에 있는 숫자가 주사위 바닥면으로 복사, 칸에 쓰여져 있는 수는 0이됨
#
# 이동할 때 마다 상단에 쓰여있는 값 구하기. 범위 밖으로 나가면 명령 무시

#  우
#   1     1
#  402 ->025
#   3     3
#   5     4
# 2 1 5 3 0 4
# 좌
#  1      1
# 402 -> 540
#  3      3
#  5      2
# 4 1 0 3 5 2
# 상
#  1     5
# 402 ->412
#  3     0
#  5     3
# 1 5 2 0 4 3
# 하
#  1     0
# 402 ->432
#  3     5
#  5     1
# 3 0 2 5 4 1
RIGHT, LEFT, UP, DOWN = 0, 1, 2, 3
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
roll = [
    [2, 1, 5, 3, 0, 4],
    [4, 1, 0, 3, 5, 2],
    [1, 5, 2, 0, 4, 3],
    [3, 0, 2, 5, 4, 1]
]
N, M, y, x, K = map(int, input().split(' '))
field = []
for _ in range(N):
    field.append(list(map(int, input().split(' '))))
cmds = list(map(int, input().split(' ')))
dice = [0] * 6

for cmd in cmds:
    # print(cmd, dice)
    # print(x,y)
    cmd = cmd-1
    next_x, next_y = x + dx[cmd], y + dy[cmd]
    if not(0 <= next_x < M and 0 <= next_y < N): continue
    next_dice = [dice[roll[cmd][i]] for i in range(6)]
    if field[next_y][next_x] == 0:
        field[next_y][next_x] = next_dice[0]
    else:
        next_dice[0] = field[next_y][next_x]
        field[next_y][next_x] = 0
    print(next_dice[5])
    dice = next_dice
    x, y = next_x, next_y

