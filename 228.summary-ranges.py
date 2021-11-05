#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#
# https://leetcode.com/problems/summary-ranges/description/
#
# algorithms
# Easy (42.87%)
# Likes:    1005
# Dislikes: 718
# Total Accepted:    214.1K
# Total Submissions: 498.9K
# Testcase Example:  '[0,1,2,4,5,7]'
#
# You are given a sorted unique integer array nums.
#
# Return the smallest sorted list of ranges that cover all the numbers in the
# array exactly. That is, each element of nums is covered by exactly one of the
# ranges, and there is no integer x such that x is in one of the ranges but not
# in nums.
#
# Each range [a,b] in the list should be output as:
#
#
# "a->b" if a != b
# "a" if a == b
#
#
#
# Example 1:
#
#
# Input: nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: The ranges are:
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"
#
#
# Example 2:
#
#
# Input: nums = [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: The ranges are:
# [0,0] --> "0"
# [2,4] --> "2->4"
# [6,6] --> "6"
# [8,9] --> "8->9"
#
#
# Example 3:
#
#
# Input: nums = []
# Output: []
#
#
# Example 4:
#
#
# Input: nums = [-1]
# Output: ["-1"]
#
#
# Example 5:
#
#
# Input: nums = [0]
# Output: ["0"]
#
#
#
# Constraints:
#
#
# 0 <= nums.length <= 20
# -2^31 <= nums[i] <= 2^31 - 1
# All the values of nums are unique.
# nums is sorted in ascending order.
#
#
#
from typing import List


# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        output = []
        j = 1
        startrangeidx = 0
        while j < len(nums):
            while j < len(nums) and nums[j] - nums[j - 1] == 1:
                j += 1
            if j - 1 != startrangeidx:
                output.append(str(nums[startrangeidx]) + "->" + str(nums[j - 1]))
            else:
                output.append(str(nums[startrangeidx]))
            if j == len(nums):
                break
            j += 1
            startrangeidx = j - 1
            if j == len(nums):
                output.append(str(nums[startrangeidx]))
                break
        return output


# @lc code=end
