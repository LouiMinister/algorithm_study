# 뱀

# NxN. 맨좌측 위치. 뱀의 길이 1. 오른쪽을 향함
# 이동
#     1. 몸길이를 늘려 다음칸에 머리를 위치
#     2. 사과가 있으면 사과가 없어지고 꼬리는 가만히
#     3. 사과가 없으면 꼬리칸 비워줌
# N,
# K
# K개의 줄에는 사과의 위치
# L 방향 변환 횟수
# X 초 후에 왼(L) 오(D) 로 회전한다는 뜻
# 몇 초에 끝나는지 계산
APPLE = 100
EMPTY = 10

N = int(input())
field = [[EMPTY] * (N+1) for _ in range(N+1)]
field[1][1] = 0
apples_cnt = int(input())
for _ in range(apples_cnt):
    in_y, in_x = map(int, input().split(' '))
    field[in_y][in_x] = APPLE
commands_cnt = int(input())
commands = dict()
for _ in range(commands_cnt):
    sec, direction = input().split(' ')
    commands[int(sec)] = direction

cur_head_x, cur_head_y = 1, 1 # 동-0 남-1 서-2 북-3
cur_tail_x, cur_tail_y = 1, 1
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
cur_sec = 0

# 초당 시뮬레이션
while True:
    # print(*field, sep='\n')
    cur_sec += 1
    cur_dir = field[cur_head_y][cur_head_x]
    # 머리 늘리기
    cur_head_y, cur_head_x = cur_head_y + dy[cur_dir], cur_head_x + dx[cur_dir]

    # 벗어나거나 사과나 빈칸이 아닌 경우 처리
    if not (0 < cur_head_y <= N and 0 < cur_head_x <= N): break
    next_cell = field[cur_head_y][cur_head_x]
    # print(next_cell)
    if not (next_cell == EMPTY or next_cell == APPLE): break

    field[cur_head_y][cur_head_x] = cur_dir
    # print(cur_dir)
    if next_cell == EMPTY:  # 꼬리 이동
        cur_tail_dir = field[cur_tail_y][cur_tail_x]
        field[cur_tail_y][cur_tail_x] = EMPTY
        cur_tail_x, cur_tail_y = cur_tail_x + dx[cur_tail_dir], cur_tail_y + dy[cur_tail_dir]

    # 현재 초에 회전 여부
    cur_command = commands.get(cur_sec)
    # print('cur_command', cur_command)
    if cur_command: # 명령 존재하면
        dir_diff = None
        if cur_command == 'D':
            dir_diff = 1
        elif cur_command == 'L':
            dir_diff = -1
        cur_dir = (cur_dir + dir_diff + 4) % 4
        field[cur_head_y][cur_head_x] = cur_dir

print(cur_sec)
