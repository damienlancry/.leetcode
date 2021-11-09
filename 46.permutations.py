#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
from typing import List


# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        self.dfs(nums, [], ret)
        return ret

    def dfs(self, nums, path, ret):
        if len(path) == len(nums):
            ret.append(path)
            return
        for i in range(len(nums)):
            if nums[i] in path:
                continue
            self.dfs(nums, path + [nums[i]], ret)


if __name__ == "__main__":
    Solution().permute([1, 2, 3])

# @lc code=end
