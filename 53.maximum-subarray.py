#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum = maxsum = nums[0]
        for num in nums[1:]:
            cursum = max(cursum + num, num)
            maxsum = max(maxsum, cursum)
        return maxsum


# @lc code=end
