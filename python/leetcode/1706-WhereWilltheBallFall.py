from typing import List


RIGHT = -1
LEFT = 1

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        w = len(grid[0])
        h = len(grid)
        res = [0] * w
        # 위치마다 떨어짐
        for d_b in range(w):
            cur_x, cur_y = d_b, 0
            while cur_y < h:
                cur_d = grid[cur_y][cur_x]
                nxt_x = cur_x + cur_d
                if (0 <= nxt_x < w) and cur_d == grid[cur_y][cur_x + cur_d]:
                    cur_x += cur_d
                    cur_y += 1
                else:
                    res[d_b] = -1
                    break
            if cur_y == h:
                res[d_b] = cur_x
        return res


print(Solution().findBall([[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]))