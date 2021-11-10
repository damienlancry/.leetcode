#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#
from typing import List


# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        if target < matrix[0][0]:
            return False
        if target > matrix[-1][-1]:
            return False
        lorow = 0
        hirow = m
        while lorow < hirow:
            midrow = (lorow + hirow) // 2
            if matrix[midrow][-1] < target < matrix[midrow + 1][0]:
                return False
            elif target <= matrix[midrow][-1]:
                hirow = midrow
            else:  # if target >= matrix[mid + 1][0]:
                lorow = midrow + 1
        assert lorow == hirow
        locol = 0
        hicol = n
        while locol < hicol:
            midcol = (locol + hicol) // 2
            if matrix[lorow][midcol] == target:
                return True
            elif matrix[lorow][midcol] > target:
                hicol = midcol
            else:
                locol = midcol + 1
        print("hello")
        return False


Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3)


# @lc code=end
