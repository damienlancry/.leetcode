#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        i = 0
        j = n - 1
        closest = nums[0] + nums[1] + nums[n - 1]
        leasterror = abs(target - closest)
        for i in range(n):
            lo = i + 1
            hi = n - 1
            while lo < hi:
                current_sum = nums[i] + nums[lo] + nums[hi]
                current_error = abs(current_sum - target)
                if current_error == 0:
                    return current_sum
                elif current_error < leasterror:
                    closest = current_sum
                    leasterror = current_error
                if current_sum > target:
                    hi -= 1
                elif current_sum < target:
                    lo += 1
        return closest


# @lc code=end
