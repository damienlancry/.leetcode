#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

from typing import List


# @lc code=start
class Solution:
    # def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    #     candidates.sort()
    #     return self.helper(candidates, target, [])

    # def helper(self, candidates: List[int], target: int, other: List[int]):
    #     if target == 0:
    #         return [other]
    #     while candidates and candidates[-1] > target:
    #         candidates.pop()
    #     if len(candidates) == 0:
    #         return []
    #     candidate = candidates.pop()
    #     ans: List[List[int]] = []
    #     w_candidate: List[List[int]] = []
    #     t = target - candidate
    #     o = other
    #     while t >= 0:
    #         o = [candidate] + o
    #         w_candidate.extend(self.helper(candidates[:], t, o))
    #         t -= candidate
    #     wo_candidate: List[List[int]] = self.helper(candidates[:], target, other)
    #     ans.extend(wo_candidate)
    #     ans.extend(w_candidate)
    #     return ans

    # dfs
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        self.dfs(candidates, target, [], ret)
        return ret

    def dfs(self, nums, target, path, ret):
        if target < 0:
            return
        if target == 0:
            ret.append(path)
            return
        for i in range(len(nums)):
            self.dfs(nums[i:], target - nums[i], path + [nums[i]], ret)


if __name__ == "__main__":
    Solution().combinationSum([2, 3, 6, 7], 7)
# @lc code=end
