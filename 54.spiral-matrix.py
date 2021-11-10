#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
from typing import List


# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        j = 0
        ans = []
        border = 0
        # interior_matrix = [[matrix[i][j] for j in range(1, n - 1)]]
        while True:
            while j < n - border:
                ans.append(matrix[i][j])
                j += 1
            if len(ans) == m * n:
                return ans
            j -= 1
            i += 1
            while i < m - border:
                ans.append(matrix[i][j])
                i += 1
            if len(ans) == m * n:
                return ans
            i -= 1
            j -= 1
            while j >= border:
                ans.append(matrix[i][j])
                j -= 1
            if len(ans) == m * n:
                return ans
            j += 1
            i -= 1
            border += 1
            while i >= border:
                ans.append(matrix[i][j])
                i -= 1
            if len(ans) == m * n:
                return ans
            i += 1
            j += 1

        #     for j in range(border, n - border):
        #         ans.append(matrix[i][j])
        #     for i in range(border + 1, m - border):
        #         ans.append(matrix[i][j])
        #     for j in range(n - border - 2, border - 1, -1):
        #         ans.append(matrix[i][j])
        #     for i in range(m - border - 2, border, -1):
        #         ans.append(matrix[i][j])
        #     border += 1
        return ans

        # ans.append(matrix[i][j])
        # i += istep
        # j += jstep
        # if j == border or j == n - border - 1:
        #     istep = jstep
        #     jstep = 0
        # if i == border and j == 0 or j or i == m - border - 1:
        #     jstep = -istep
        #     istep = 0
        # if i == m - border and j == border:
        #     border += 1
        # return ans


if __name__ == "__main__":
    Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# @lc code=end
