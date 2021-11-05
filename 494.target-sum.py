#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#
# @lc code=start
class Solution:
    # brute force
    # def findTargetSumWays(self, nums: List[int], target: int) -> int:
    #     return self.helper(nums, target, len(nums) - 1, 0)

    # def helper(self, nums, target, i, j):
    #     if i < 0:
    #         if j == target:
    #             return 1
    #         else:
    #             return 0

    #     positive = self.helper(nums, target, i - 1, j + nums[i])
    #     negative = self.helper(nums, target, i - 1, j - nums[i])
    #     return positive + negative

    # dynamic programming: memoization
    # def findTargetSumWays(self, nums: List[int], target: int) -> int:
    #     return self.helper(nums, target, len(nums) - 1, 0, dict())

    # def helper(self, nums, target, i, j, memo):
    #     if (i, j) in memo:
    #         return memo[(i, j)]
    #     if i < 0:
    #         if j == target:
    #             return 1
    #         else:
    #             return 0

    #     positive = self.helper(nums, target, i - 1, j + nums[i], memo)
    #     negative = self.helper(nums, target, i - 1, j - nums[i], memo)
    #     memo[(i, j)] = positive + negative
    #     return memo[(i, j)]

    # dynamic programming: tabulation - bottom up
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        from collections import defaultdict

        if not nums:
            return 0
        n = len(nums)
        s = target
        dp = {0: 1}  # one way to make 0 with []
        for num in nums:
            tmp = defaultdict(int)
            for s, n in dp.items():
                tmp[s + num] += n
                tmp[s - num] += n
            dp = tmp
        return dp[target]


# @lc code=end
