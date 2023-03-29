from itertools import product

MIS = lambda: map(int,input().split())
def union(sets):
    res = set()
    for s in sets: res|= s
    return res

def sight(i0, j0):
    for di, dj in (1,0), (-1,0), (0,1), (0,-1):
        i, j = i0, j0
        seen = set()
        while 0<=i<n and 0<=j<m and grid[i][j] != 6:
            seen.add((i,j))
            i+= di; j+= dj
        yield seen

n, m = MIS()
grid = [list(MIS()) for i in range(n)]
camera = []
empty = 0
for i in range(n):
    for j in range(m):
        c = grid[i][j]
        if c == 6: continue
        empty+= 1
        if c == 0: continue
        D, U, R, L = sight(i, j)
        if c == 1: camera.append([D,U,R,L])
        elif c == 2: camera.append([D|U, R|L])
        elif c == 3: camera.append([U|R, U|L, D|R, D|L])
        elif c == 4: camera.append([D|U|R, D|U|L, R|L|U, R|L|D])
        else: camera.append([D|U|R|L])
print(min(empty - len(union(P)) for P in product(*camera)))