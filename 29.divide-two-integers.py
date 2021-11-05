#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
min_int = -(2 ** 31)
max_int = 2 ** 31 - 1


def overflows(i):
    return not min_int <= i <= max_int


def isEven(n):
    return n ^ 1 == n + 1


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == min_int and divisor == -1:
            return max_int
        a, b, res = abs(dividend), abs(divisor), 0
        for x in range(31, -1, -1):
            if (a >> x) - b >= 0:
                res += 1 << x
                a -= b << x
        return res if (dividend > 0) == (divisor > 0) else -res


# @lc code=end
