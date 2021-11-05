#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#
# https://leetcode.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (55.81%)
# Likes:    2475
# Dislikes: 130
# Total Accepted:    488.7K
# Total Submissions: 874.3K
# Testcase Example:  '5'
#
# Given an integer numRows, return the first numRows of Pascal's triangle.
#
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it as shown:
#
#
# Example 1:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:
# Input: numRows = 1
# Output: [[1]]
#
#
# Constraints:
#
#
# 1 <= numRows <= 30
#
#
#

from typing import List


# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        res = [[1], [1, 1]]
        for _ in range(2, numRows):
            res.append([1] + [i + j for i, j in zip(res[-1][:-1], res[-1][1:])] + [1])
        return res


# @lc code=end
