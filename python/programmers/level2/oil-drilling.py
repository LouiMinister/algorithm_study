# [PCCP 기출문제] 2번 / 석유 시추

from collections import deque

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

def solution(land):
    width = len(land[0])
    height = len(land)
    
    cntPerLand = [0 for _ in range(width)]
    vis = [[False for _ in range(width)] for _ in range(height)]
    
    def isOutOfBound(x, y):
        return x < 0 or y < 0 or x >= width or y >= height
    
    def bfs(x, y):
        if land[y][x] == 0: return
        if vis[y][x]: return
        vis[y][x] = True        
        visitedCol = set()
        visitedCol.add(x)
        oilCnt = 1
        dq = deque()
        
        dq.append((x, y))
        while dq:
            curX, curY = dq.popleft()
            for d in range(4):
                nextX, nextY = curX + dx[d], curY + dy[d]
                if isOutOfBound(nextX, nextY): continue
                if vis[nextY][nextX]: continue
                if land[nextY][nextX] == 0: continue # 빈 땅
                # print(nextX, nextY)
                
                vis[nextY][nextX] = True
                dq.append((nextX, nextY))
                visitedCol.add(nextX)
                oilCnt += 1
        
        for col in visitedCol:
            cntPerLand[col] += oilCnt
            
        # print(oilCnt)
        # print(cntPerLand)
                
    for ix in range(width):
        for iy in range(height):
            bfs(ix, iy)
            
    return max(cntPerLand)
    # print(max(enumerate(cntPerLand), key= lambda x: x[1]))
            
            
        
        
    
    