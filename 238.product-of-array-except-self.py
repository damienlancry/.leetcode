#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        curprod = 1
        for num in nums:
            left.append(curprod)
            curprod *= num
        right = []
        curprod = 1
        for num in reversed(nums):
            right.append(curprod)
            curprod *= num
        return [l * r for l, r in zip(left, reversed(right))]


# @lc code=end
