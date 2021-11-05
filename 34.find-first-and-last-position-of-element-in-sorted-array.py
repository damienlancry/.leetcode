#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        if len(nums) == 1:
            return [0, 0] if nums[0] == target else [-1, -1]
        lo, idx, hi = binary_search(target, nums, 0, len(nums) - 1)
        if idx == -1:
            return [-1, -1]
        else:
            return [
                binary_search_left(target, nums, lo, idx),
                binary_search_right(target, nums, idx, hi),
            ]


def binary_search_left(target, nums, lo, hi):
    assert target == nums[hi]  # target is the max value of the sub array
    while lo < hi:
        mid = (lo + hi) // 2
        if target == nums[mid]:
            if nums[mid - 1] < nums[mid]:  # found first occurrence
                return mid
            else:
                hi = mid
        else:  # nums[mid] < target
            lo = mid + 1
    return lo if nums[lo] == target else -1


def binary_search_right(target, nums, lo, hi):
    assert target == nums[lo]  # target is the min value of the sub array
    while lo < hi:
        mid = (lo + hi) // 2
        if target == nums[mid]:
            if nums[mid + 1] > nums[mid]:  # found last occurrence
                return mid
            else:
                lo = mid + 1
        else:  # nums[mid] < target
            hi = mid
    return lo if nums[lo] == target else -1


def binary_search(target, nums, lo, hi):
    while lo < hi:
        mid = (lo + hi) // 2
        print("bs:lomidhi", lo, mid, hi)
        if target == nums[mid]:
            return lo, mid, hi
        if target > nums[mid]:
            lo = mid + 1
        else:
            hi = mid

    print("lomidhi", lo, mid, hi)
    return (lo, lo, hi) if target == nums[lo] else (-1, -1, -1)


# @lc code=end
