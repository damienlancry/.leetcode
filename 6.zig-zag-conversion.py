#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        l = [""] * numRows
        index, step = 0, 1
        for c in s:
            l[index] += c
            if index == 0:
                step = 1
            if index == numRows - 1:
                step = -1
            index += step
        return "".join(l)


# @lc code=end
