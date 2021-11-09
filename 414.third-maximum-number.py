#
# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
#

# @lc code=start
import random


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        if len(nums) < 3:
            return max(nums)
        return self.quickselect(list(set(nums)), 3)

    def quickselect(self, nums, k):
        pivot = nums[random.randint(0, len(nums) - 1)]
        left = []
        right = []
        for num in nums:
            if num <= pivot:
                left.append(num)
            else:
                right.append(num)
        if len(right) == k - 1:
            return pivot
        elif len(right) >= k:
            return self.quickselect(right, k)
        else:
            return self.quickselect(left, k - len(right))


# @lc code=end
