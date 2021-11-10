#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        zeroedrows = set()
        zeroedcols = set()
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    zeroedrows.add(row)
                    zeroedcols.add(col)
        for row in zeroedrows:
            for col in range(n):
                matrix[row][col] = 0
        for col in zeroedcols:
            for row in range(m):
                matrix[row][col] = 0
        return matrix


# @lc code=end
