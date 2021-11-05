#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            digits[-1] = digits[-1] + 1
            return digits
        end = len(digits) - 1
        i = 0
        while end - i >= 0 and digits[end - i] == 9:
            digits[end - i] = 0
            i += 1
        if end - i < 0:
            return [1] + digits
        else:
            digits[end - i] = digits[end - i] + 1
            return digits


# @lc code=end
