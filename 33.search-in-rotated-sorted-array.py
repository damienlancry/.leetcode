#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        p = find_pivot(nums)
        if nums[p] <= target <= nums[-1]:
            return binary_search(target, nums, p, len(nums) - 1)
        elif nums[0] <= target <= nums[p - 1]:
            return binary_search(target, nums, 0, p - 1)
        else:
            return -1


def binary_search(target, nums, lo, hi):
    while lo < hi:
        mid = (lo + hi) // 2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            lo = mid + 1
        else:
            hi = mid
    return lo if nums[lo] == target else -1


def find_pivot(nums):
    n = len(nums)
    lo = 0
    hi = n - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[lo] <= nums[mid] <= nums[hi]:
            return lo
        elif nums[lo] > nums[mid]:
            hi = mid
        else:
            lo = mid + 1
    return lo


# @lc code=end
