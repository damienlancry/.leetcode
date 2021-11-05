#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set()
        intersect = set()
        for num in nums1:
            set1.add(num)
        for num in nums2:
            if num in set1:
                intersect.add(num)
        return intersect


# @lc code=end
