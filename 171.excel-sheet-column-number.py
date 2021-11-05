#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#
# https://leetcode.com/problems/excel-sheet-column-number/description/
#
# algorithms
# Easy (57.26%)
# Likes:    1674
# Dislikes: 200
# Total Accepted:    376.7K
# Total Submissions: 657.5K
# Testcase Example:  '"A"'
#
# Given a string columnTitle that represents the column title as appear in an
# Excel sheet, return its corresponding column number.
#
# For example:
#
#
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28
# ...
#
#
#
# Example 1:
#
#
# Input: columnTitle = "A"
# Output: 1
#
#
# Example 2:
#
#
# Input: columnTitle = "AB"
# Output: 28
#
#
# Example 3:
#
#
# Input: columnTitle = "ZY"
# Output: 701
#
#
# Example 4:
#
#
# Input: columnTitle = "FXSHRXW"
# Output: 2147483647
#
#
#
# Constraints:
#
#
# 1 <= columnTitle.length <= 7
# columnTitle consists only of uppercase English letters.
# columnTitle is in the range ["A", "FXSHRXW"].
#
#
#

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ordA = ord("A")
        return sum((ord(c) - ordA + 1) * 26 ** p for p, c in enumerate(columnTitle[::-1]))


# @lc code=end
