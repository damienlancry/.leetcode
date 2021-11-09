#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
def pprint(matrix):
    for row in matrix:
        print(row)
    print()


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2):
            tmp = matrix[i][i]
            matrix[i][i] = matrix[n - 1 - i][i]
            matrix[n - 1 - i][i] = matrix[n - 1 - i][n - 1 - i]
            matrix[n - 1 - i][n - 1 - i] = matrix[i][n - 1 - i]
            matrix[i][n - 1 - i] = tmp
            for j in range(i + 1, n - 1 - i):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = tmp
        return matrix


# @lc code=end
