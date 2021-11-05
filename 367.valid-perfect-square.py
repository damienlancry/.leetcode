#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        lo = 0
        hi = num // 2
        while lo <= hi:
            mid = (hi + lo) // 2
            print(lo, mid, hi)
            mid2 = mid ** 2
            if mid2 == num:
                return True
            elif mid2 > num:
                hi = mid - 1
            else:
                lo = mid + 1
            print(lo, hi)
        return False


# @lc code=end
