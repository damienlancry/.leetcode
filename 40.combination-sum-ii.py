#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#
from typing import List


# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ret = []
        self.dfs(candidates, target, 0, [], ret)
        return ret

    def dfs(self, nums, target, index, path, ret):
        if target < 0:
            return
        if target == 0:
            ret.append(path)
            return
        i = index
        while i < len(nums) and target >= nums[i]:
            # for i in range(index, len(nums)):
            # if target < nums[i]:
            # break
            j = 1
            while i + j < len(nums) and nums[i + j] == nums[i]:
                j += 1
            for k in range(j, 0, -1):
                self.dfs(nums, target - k * nums[i], i + j, path + k * [nums[i]], ret)
            i += j


if __name__ == "__main__":
    Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
# @lc code=end
