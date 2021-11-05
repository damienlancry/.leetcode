#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cursum = maxsum = sum(nums[:k])
        for i in range(k, len(nums)):
            cursum += nums[i]
            cursum -= nums[i - k]
            maxsum = max(maxsum, cursum)
        return float(maxsum) / k


# @lc code=end
