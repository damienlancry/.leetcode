#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

from typing import List


# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []
        self.dfs(nums, [False for _ in range(len(nums))], [], ret)
        return ret

    def dfs(self, nums, used, path, ret):
        if len(nums) == len(path):
            ret.append(path)
            return
        for i in range(len(nums)):
            if used[i] or i > 0 and nums[i - 1] == nums[i] and not used[i - 1]:
                continue
            self.dfs(nums, used[:i] + [True] + used[i + 1 :], path + [nums[i]], ret)


# @lc code=end
