#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
def find_median(nums):
    n = len(nums)
    if n % 2 == 1:
        med = nums[n // 2]
    else:
        med = float(nums[n // 2 - 1] + nums[n // 2]) / 2
    return med


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        if n < m:
            nums1, nums2, m, n = nums2, nums1, n, m
        imax = m
        imin = 0
        half = (m + n + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = half - i
            if i < m and nums2[j - 1] > nums1[i]:
                imin = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                imax = i - 1
            else:
                if i == 0:
                    maxleft = nums2[j - 1]
                elif j == 0:
                    maxleft = nums1[i - 1]
                else:
                    maxleft = max(nums1[i - 1], nums2[j - 1])
                if (m + n) % 2 == 1:
                    return maxleft
                if i == m:
                    minright = nums2[j]
                elif j == n:
                    minright = nums1[i]
                else:
                    minright = min(nums1[i], nums2[j])
                return float(maxleft + minright) / 2


# @lc code=end
