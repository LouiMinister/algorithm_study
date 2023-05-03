from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        h = len(matrix)
        w = len(matrix[0])
        memo = [[False] * w for _ in range(h)]
        cur_w, cur_h = 0, 0
        res.append(matrix[0][0])
        memo[cur_h][cur_w] = True
        while len(res) != w * h:
            while cur_w + 1 < w and not memo[cur_h][cur_w + 1]:
                cur_w += 1
                memo[cur_h][cur_w] = True
                res.append(matrix[cur_h][cur_w])
            while cur_h + 1 < h and not memo[cur_h + 1][cur_w]:
                cur_h += 1
                memo[cur_h][cur_w] = True
                res.append(matrix[cur_h][cur_w])
            while cur_w - 1 >= 0 and not memo[cur_h][cur_w - 1]:
                cur_w -= 1
                memo[cur_h][cur_w] = True
                res.append(matrix[cur_h][cur_w])
            while cur_h - 1 >= 0 and not memo[cur_h - 1][cur_w]:
                cur_h -= 1
                memo[cur_h][cur_w] = True
                res.append(matrix[cur_h][cur_w])
            print(res)
        return res

    # left, right, top, bottom 을 이용하여 찾기
    def optimized(self, matrix: List[List[int]]) -> List[int]:
        res = []
        h = len(matrix)
        w = len(matrix[0])
        top, bottom, left, right = 0, h - 1, 0, w - 1
        while top < bottom or left < right:
            for w_i in range(left, right + 1):
                res.append(matrix[top][w_i])
            top += 1
            for h_i in range(top, bottom + 1):
                res.append(matrix[h_i][right])
            right -= 1
            for w_i in range(right, left - 1, -1):
                res.append(matrix[bottom][w_i])
            bottom -= 1
            for h_i in range(bottom, top - 1, -1):
                res.append(matrix[h_i][left])
            left += 1
        return res

# print("HI")
print(Solution().optimized([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
