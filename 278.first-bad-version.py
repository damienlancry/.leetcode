#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        hi = n
        lo = 0
        while lo < hi:
            mid = (hi + lo) // 2
            midp1 = mid + 1
            bad = isBadVersion(mid)
            badp1 = isBadVersion(midp1)
            if not bad and badp1:
                return midp1
            elif not bad:  # and not badp1
                lo = midp1
            else:  # bad and badp1
                hi = mid


# @lc code=end
