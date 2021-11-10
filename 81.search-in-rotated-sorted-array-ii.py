#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 1:
            return target == nums[0]
        if nums[-1] < target < nums[0]:
            return False
        lo = 0
        hi = len(nums) - 1
        if nums[lo] < nums[hi]:
            pivot = nums[lo]
        else:
            while lo < hi and nums[lo] == nums[hi]:
                lo += 1
            while lo < hi:
                mid = (lo + hi) // 2
                # if nums[lo] == nums[mid] == nums[hi]:
                # there must be one side that has only one number and the other that has different numbers
                # try left
                # on est dans la merde
                if nums[mid] <= nums[hi]:  # pivot is on the left
                    hi = mid
                elif nums[mid] >= nums[lo]:  # pivot is on the right
                    lo = mid + 1
                else:
                    print("que pasa")
            print(lo, hi)
            pivot = nums[lo]
            if target == pivot:
                return True
            elif nums[lo] <= target <= nums[-1]:  # target is on the right
                hi = len(nums) - 1
            else:  # target is on the left
                lo = 0
        while lo < hi:
            mid = (lo + hi) // 2
            print(lo, hi, mid, nums[mid])
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return True if nums[lo] == target else False


# @lc code=end
