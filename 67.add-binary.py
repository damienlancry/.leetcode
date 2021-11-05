#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def pad(a, b):
            if len(a) == len(b):
                return a, b
            if len(a) > len(b):
                return a, "0" * (len(a) - len(b)) + b
            return pad(b, a)

        a, b = pad(a, b)
        end = len(b) - 1
        i = 0
        carry = 0
        res = ""
        while end - i >= 0:
            sub = int(a[end - i]) + int(b[end - i]) + carry
            carry, sub = divmod(sub, 2)
            res = str(sub) + res
            i += 1
        if carry == 1:
            return "1" + res
        return res


# @lc code=end
