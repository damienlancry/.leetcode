#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = dict()
        for c in s:
            if c in count:

                count[c] += 1
            else:
                count[c] = 1
        for i, c in enumerate(s):
            if count[c] == 1:
                return i
        return -1


# @lc code=end
