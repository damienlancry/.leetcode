#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            div, mod = divmod(n, 10)
            n = mod ** 2
            while div > 9:
                div, mod = divmod(div, 10)
                n += mod ** 2
            n += div ** 2
            if n in seen:
                return False
            seen.add(n)
        return True


# @lc code=end
