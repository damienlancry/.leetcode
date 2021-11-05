#
# @lc app=leetcode id=374 lang=python3
#
# [374] Guess Number Higher or Lower
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:
        hi = n
        lo = 0
        while lo <= hi:
            mid = (hi + lo) // 2
            guess_ = guess(mid)
            if guess_ == 0:
                return mid
            elif guess_ == 1:
                lo = mid + 1
            else:
                hi = mid - 1


# @lc code=end
