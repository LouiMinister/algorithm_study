# 상하좌우
pos = [1, 1]
n = int(input())
cmds = input().split(' ')
direction = {
    'R': (0, 1),
    'L': (0, -1),
    'U': (-1, 0),
    'D': (1, 0)
}

for cmd in cmds:
    d = direction[cmd]
    next_pos = [sum(x) for x in zip(pos, d)]
    is_in_boundary = all(0 < ele < n for ele in next_pos)
    if is_in_boundary:
        pos = next_pos

print(pos)
