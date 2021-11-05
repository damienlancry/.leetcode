#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        if target > nums[hi]:
            return hi + 1
        if target < nums[lo]:
            return 0
        while lo < hi:
            if nums[lo] == target:
                return lo
            if nums[hi] == target:
                return hi
            mid = (hi + lo) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                hi = mid
            else:
                lo = mid + 1
        return lo


# @lc code=end
