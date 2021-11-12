#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()

        def dfs(index, path):
            ret.append(path)
            i = index
            while i < len(nums):
                j = 1
                while i + j < len(nums) and nums[i] == nums[i + j]:
                    j += 1
                for k in range(1, j + 1):
                    dfs(i + j, path + k * [nums[i]])
                i += j

        dfs(0, [])
        return ret


# @lc code=end
