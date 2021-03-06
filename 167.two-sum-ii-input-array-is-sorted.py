#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
#
# algorithms
# Easy (55.86%)
# Likes:    2634
# Dislikes: 730
# Total Accepted:    565.2K
# Total Submissions: 1M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers numbers that is already sorted in ascending order,
# find two numbers such that they add up to a specific target number.
#
# Return the indices of the two numbers (1-indexed) as an integer array answer
# of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.
#
# You may assume that each input would have exactly one solution and you may
# not use the same element twice.
#
#
# Example 1:
#
#
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
#
#
# Example 2:
#
#
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
#
#
# Example 3:
#
#
# Input: numbers = [-1,0], target = -1
# Output: [1,2]
#
#
#
# Constraints:
#
#
# 2 <= numbers.length <= 3 * 10^4
# -1000 <= numbers[i] <= 1000
# numbers is sorted in increasing order.
# -1000 <= target <= 1000
# Only one valid answer exists.
#
#
#
from typing import List

# @lc code=start
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         hashmap = {}
#         for i, number in enumerate(numbers):
#             if number in hashmap:
#                 return [hashmap[number], i + 1]
#             hashmap[target - number] = i + 1


# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         left, right = 0, len(numbers) - 1
#         while left < right:
#             sum = numbers[left] + numbers[right]
#             if sum == target:
#                 return [left + 1, right + 1]
#             if sum < target:
#                 left += 1
#             else:
#                 right -= 1


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            left, right = i + 1, len(numbers) - 1
            tmp = target - numbers[i]
            while left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] == tmp:
                    return [i + 1, mid + 1]
                if numbers[mid] < tmp:
                    left = mid + 1
                else:
                    right = mid - 1


# @lc code=end
