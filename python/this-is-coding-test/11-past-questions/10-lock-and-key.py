# 자물쇠와 열쇠

def solution(key, lock):
    rotated_key = key
    for r in range(4):
        rotated_key = rotate_key(rotated_key)
        print('!!!!')
        for dx in range(-len(key) + 1, len(lock)):
            for dy in range(-len(key) + 1, len(lock)):
                moved_key = move_key(rotated_key, dx, dy, len(lock))
                print(dx, dy)
                print(moved_key,)
                if is_match(moved_key, lock):
                    return True
    return False

def move_key(key, dx, dy, lock_size):
    res = [[0 for _ in range(lock_size)] for _ in range(lock_size)]
    # dx = -1 -> s_x =1
    # dx = 1 -> sx = 1
    for y in range(max(0, 0 - dy), min(lock_size, lock_size - dy)):
        for x in range(max(0,0 - dx), min(lock_size, lock_size - dx)):
            if 0<=y<len(key) and 0<=x<len(key):
                res[y+dy][x+dx] = key[y][x]
    return res

def rotate_key(key):
    key_len = len(key)
    res = [[0 for _ in range(key_len)] for _ in range(key_len)]
    for i in range(0, key_len):
        for j in range(0, key_len):
            res[i][j] = key[key_len-1-j][i]
    return res

def is_match(key, lock):
    lock_len = len(lock)
    for y in range(lock_len):
        for x in range(lock_len):
            if key[y][x] == lock[y][x]:
                return False
    return True

print(solution([[1,1,1],[1,1,1],[1,1,1]], [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]))