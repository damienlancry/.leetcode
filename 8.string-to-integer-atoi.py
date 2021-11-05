#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0
        # step 1
        i = 0
        while i < len(s) and s[i] == " ":
            i += 1
        if i == len(s):
            return 0
        # step 2
        if s[i] == "+":
            sign = 1
            i += 1
        elif s[i] == "-":
            sign = -1
            i += 1
        elif s[i] in "0123456789":
            sign = 1
        else:
            return 0
        res = 0
        while i < len(s) and s[i] in "0123456789":
            res = res * 10 + int(s[i])
            i += 1
        if sign == 1:
            res = res if res <= 2 ** 31 - 1 else 2 ** 31 - 1
        else:
            res = res if res <= 2 ** 31 else 2 ** 31

        return sign * res


# @lc code=end
