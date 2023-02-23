# 로봇 시뮬레이션

W, H = map(int, input().split(' '))
robot_cnt, command_cnt = map(int, input().split(' '))

field = [[None] * (W+1) for _ in range(H+1)]
robots = [None] * (robot_cnt + 1)

def turn(robot_idx, direction, repeat_cnt):
    global robots
    dirs = None
    if direction == 'R':
        dirs = ['N', 'E', 'S', 'W']
    if direction == 'L':
        dirs = ['N', 'W', 'S', 'E']
    robot = robots[robot_idx]
    next_dir_idx = (dirs.index(robot[2]) + repeat_cnt) % 4
    robots[robot_idx] = (robot[0], robot[1], dirs[next_dir_idx])

def forward(robot_idx, repeat_cnt):
    global robots, field
    dxdy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dirs = ['N', 'E', 'S', 'W']
    robot = robots[robot_idx]
    cur_robot_direction = robot[2]
    robot_direction_idx = dirs.index(cur_robot_direction)
    dx, dy = dxdy[robot_direction_idx]
    nx, ny = None, None
    for i in range(1, repeat_cnt+1):
        nx, ny = robot[0] + dx * i, robot[1] + dy * i
        if not(0 < nx <= W and 0 < ny <= H):
            print(f'Robot {robot_idx} crashes into the wall')
            exit(0)
        if field[ny][nx] != None:
            print(f'Robot {robot_idx} crashes into robot {field[ny][nx]}')
            exit(0)
    field[robot[1]][robot[0]] = None
    field[ny][nx] = robot_idx
    robots[robot_idx] = (nx, ny, robot[2])


for i in range(1, robot_cnt + 1):
    in1, in2, in3 = input().split(' ')
    robots[i] = (int(in1), int(in2), in3)
    field[int(in2)][int(in1)] = i

for i in range(command_cnt):
    # print(robots)
    # print(field)
    robot_idx, command, repeat_cnt = input().split(' ')
    robot_idx, repeat_cnt = int(robot_idx), int(repeat_cnt)
    if command == 'F':
        forward(robot_idx, repeat_cnt)
    if command == 'L' or command == 'R':
        turn(robot_idx, command, repeat_cnt)

print('OK')

