#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#
from typing import List


# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        step = 1
        row, col, drow, dcol = 0, 0, 0, 1
        for step in range(1, n * n + 1):
            matrix[row][col] = step
            if matrix[(row + drow) % n][(col + dcol) % n]:
                drow, dcol = dcol, -drow
            row += drow
            col += dcol
        return matrix


Solution().generateMatrix(3)
# @lc code=end
