#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#
from typing import List


# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = self.sortbyfirst(intervals)
        return self._merge(intervals)

    def sortbyfirst(self, intervals):
        if len(intervals) <= 1:
            return intervals
        pivot = intervals[0]
        left = []
        right = []
        for interval in intervals[1:]:
            if interval[0] < pivot[0] or interval[0] == pivot[0] and interval[1] < pivot[1]:
                left.append(interval)
            else:
                right.append(interval)
        return self.sortbyfirst(left) + [pivot] + self.sortbyfirst(right)

    def _merge(self, intervals):
        ans = []
        i = 0
        j = 1
        while i < len(intervals):
            starti, endi = intervals[i]
            j = i + 1
            while j < len(intervals) and endi >= intervals[j][0]:
                endi = max(endi, intervals[j][1])
                j += 1
            ans.append([starti, endi])
            i = j

        return ans


Solution().merge([[1, 4], [2, 3]])
Solution().merge([[1, 4], [1, 5]])
Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]])

# @lc code=end
