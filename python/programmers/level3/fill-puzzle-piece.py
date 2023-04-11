# 3 <= 행 열 <= 50
# 1 <= 퍼즐 개수 <= 6
# table의 크기 = game_board의 크기
# table에는 반드시 하나 이상의 블록
# game_board에는 반드시 하나 이상의 빈칸

# 회전, 뒤집 가능.
# 새로 넣은 퍼즐 조각과 인접한 칸이 비면 안됨
from collections import deque

blocks = []
game_board = [[]]
table = [[]]
N = 0


def inBound(x, y):
    global N
    return 0 <= x < N and 0 <= y < N


def bfs(x, y, vis):
    global table, N
    q = deque()
    block = set([(x, y)])
    q.append((x, y))  # cur pos & trace
    while q:
        cur_x, cur_y = q.popleft()
        if vis[cur_y][cur_x]: continue
        vis[cur_y][cur_x] = True
        for d_x, d_y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nxt_x, nxt_y = cur_x + d_x, cur_y + d_y
            if not inBound(nxt_x, nxt_y): continue
            if vis[nxt_y][nxt_x]: continue
            if table[nxt_y][nxt_x] == 0: continue
            block.add((nxt_x, nxt_y))
            q.append((nxt_x, nxt_y))
    return block


def initBlocks(table):
    global blocks, N
    vis = [[False] * N for _ in range(N)]
    for h_i in range(N):
        for w_i in range(N):
            if table[h_i][w_i] == 0: continue
            if vis[h_i][w_i]: continue
            block = bfs(w_i, h_i, vis)
            if block: blocks.append(block)


# def isFit(block):

def spin(block):
    global N
    spined = set()
    min_x, min_y = N, N
    for cell in block:
        spined.add((cell[1], -cell[0]))
        min_x, min_y = min(min_x, cell[1]), min(min_y, -cell[0])
    formated = set()
    for cell in spined:
        formated.add((cell[0] - min_x, cell[1] - min_y))
    return formated


def move(block):
    global N
    max_x, max_y = -N, -N
    for cell in block:
        max_x = max(max_x, cell[0])
        max_y = max(max_y, cell[1])
    for dy in range(N - max_y):
        for dx in range(N - max_x):
            moved = set()
            for cell in block:
                moved.add((cell[0] + dx, cell[1] + dy))
            yield moved


def isFit(block):
    global game_board
    for cell in block:
        c_x, c_y = cell[0], cell[1]
        if game_board[c_y][c_x] == 1: return False
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nxt_x, nxt_y = c_x + dx, c_y + dy
            if not inBound(nxt_x, nxt_y): continue
            # 만약에 비어있는데, cell에 없으면 False
            if game_board[nxt_y][nxt_x] == 0 and (nxt_x, nxt_y) not in block:
                return False
    return True


def fill(block):
    global game_board
    for c_x, c_y in block:
        game_board[c_y][c_x] = 1


def action(block):
    global game_board, N
    for spin_cnt in range(4):
        block = spin(block)
        for moved_block in move(block):
            if isFit(moved_block):
                fill(moved_block)
                return len(block)
    return 0


def solution(_game_board, _table):
    global game_board, table, N, blocks
    game_board = _game_board
    table = _table
    N = len(game_board)
    initBlocks(table)

    # print(blocks)
    res = 0
    for block in blocks:
        action_res = action(block)
        if action_res > 0:
            # print('fitblock', block, action_res)
            res += action_res
    # print('res!',res)
    return res

    # 1 블럭 정보 가져오기
    # 2 블럭 회전하기
    # 3 블럭 fit 여부 반환

    # 제일 많이채워 넣을 경우, 총 몇칸 채울 수 있는지