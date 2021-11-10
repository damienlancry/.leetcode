#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        countzeros = 0
        countones = 0
        for num in nums:
            if num == 0:
                countzeros += 1
            elif num == 1:
                countones += 1
        for i in range(countzeros):
            nums[i] = 0
        for i in range(countzeros, countzeros + countones):
            nums[i] = 1
        for i in range(countones + countzeros, len(nums)):
            nums[i] = 2


# @lc code=end
