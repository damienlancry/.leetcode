#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#
# https://leetcode.com/problems/pascals-triangle-ii/description/
#
# algorithms
# Easy (52.71%)
# Likes:    1342
# Dislikes: 222
# Total Accepted:    371.2K
# Total Submissions: 703.7K
# Testcase Example:  '3'
#
# Given an integer rowIndex, return the rowIndex^th (0-indexed) row of the
# Pascal's triangle.
#
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it as shown:
#
#
# Example 1:
# Input: rowIndex = 3
# Output: [1,3,3,1]
# Example 2:
# Input: rowIndex = 0
# Output: [1]
# Example 3:
# Input: rowIndex = 1
# Output: [1,1]
#
#
# Constraints:
#
#
# 0 <= rowIndex <= 33
#
#
#
# Follow up: Could you optimize your algorithm to use only O(rowIndex) extra
# space?
#
#

from typing import List


# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascal = [[1] * (i + 1) for i in range(rowIndex + 1)]
        for i in range(1, rowIndex + 1):
            for j in range(1, i):
                pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
        return pascal[rowIndex]


# @lc code=end
