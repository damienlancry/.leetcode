#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        if newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals
        if newInterval[0] > intervals[-1][-1]:
            return intervals + [newInterval]
        i = 0
        while i < len(intervals) and intervals[i][0] < newInterval[0]:
            i += 1
        intervals = intervals[:i] + [newInterval] + intervals[i:]
        i = 1
        starti, endi = intervals[i - 1]
        ans = []
        while i < len(intervals):
            if endi < intervals[i][0]:
                ans.append([starti, endi])
                starti, endi = intervals[i]
            else:
                endi = max(endi, intervals[i][1])
            i += 1
        ans.append([starti, endi])
        return ans


# @lc code=end
