#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        lo = 0
        hi = x
        while lo < hi:
            mid = (hi + lo) // 2
            mid2 = mid ** 2
            midp12 = (mid + 1) ** 2
            if mid2 < x < midp12:
                return mid
            if mid2 == x:
                return mid
            if midp12 == x:
                return mid + 1
            if x > midp12:
                lo = mid + 1
            elif x < mid2:
                hi = mid
        return lo


# @lc code=end
