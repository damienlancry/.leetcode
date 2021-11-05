#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = n - 2
        while k >= 0:
            if nums[k] < nums[k + 1]:
                break
            k -= 1
        if k == -1:
            k = 0
            while k <= n // 2 - 1:
                nums[k], nums[-1 - k] = nums[-1 - k], nums[k]
                k += 1
            return
        l = n - 1
        while l > k:
            if nums[k] < nums[l]:
                break
            l -= 1
        nums[k], nums[l] = nums[l], nums[k]
        i = 0
        while k + 1 + i <= (n + k + 1) // 2 - 1:
            nums[k + 1 + i], nums[-1 - i] = nums[-1 - i], nums[k + 1 + i]
            i += 1


# @lc code=end
