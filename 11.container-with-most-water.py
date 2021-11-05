#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        maxvolume = 0
        i = 0
        j = n - 1
        while i < j:
            volume = (j - i) * min(height[i], height[j])
            maxvolume = max(maxvolume, volume)
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return maxvolume


# @lc code=end
