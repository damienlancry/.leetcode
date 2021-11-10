#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []  # [[], nums]
        self.dfs(nums, 0, [], ret)
        return ret

    def dfs(self, nums, index, path, ret):
        ret.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i + 1, path + [nums[i]], ret)


# @lc code=end
