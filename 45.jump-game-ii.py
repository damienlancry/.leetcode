#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#
from typing import List


# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        steps = 1
        l, r = 0, nums[0]
        while r < len(nums) - 1:
            steps += 1
            l, r = r, max(i + nums[i] for i in range(l, r + 1))
        return steps


# @lc code=end
