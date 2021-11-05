#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
class Solution:
    # def rob(self, nums: List[int]) -> int:
    #     dorobfirst = self.helper(nums[1:-1], len(nums[1:-1]) - 1, nums[0])
    #     doroblast = self.helper(nums[1:-1], len(nums[1:-1]) - 1, nums[-1])
    #     dontrobfirst = self.helper(nums[1:], len(nums[1:]) - 1, 0)
    #     dontroblast = self.helper(nums[:-1], len(nums[:-1]) - 1, 0)
    #     return max(dorobfirst, dontrobfirst, doroblast, dontroblast)

    # def helper(self, nums, i, j):
    #     if i < 0:
    #         return j
    #     do = self.helper(nums, i - 1, j + nums[i])
    #     dont = self.helper(nums, i - 1, j)
    #     return max(do, dont)

    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        left = nums[1:]
        right = nums[:-1]
        return max(self.helper(left), self.helper(right))

    def helper(self, nums) -> int:
        prev = 0
        curr = nums[0]
        for i in range(1, len(nums)):
            curr, prev = max(prev + nums[i], curr), curr
        return curr


# @lc code=end
