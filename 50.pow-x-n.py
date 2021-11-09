#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        print(x, n)
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == 2:
            return x * x
        if n < 0:
            return 1 / self.myPow(x, -n)
        div, mod = n // 2, n % 2
        return self.myPow(self.myPow(x, div), 2) * self.myPow(x, mod)


# @lc code=end
