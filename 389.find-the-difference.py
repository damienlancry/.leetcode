#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#

# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        seen = dict()
        for c in s:
            if c in seen:
                seen[c] += 1
            else:
                seen[c] = 1
        print(seen)
        for c in t:
            if c not in seen:
                return c
            else:
                seen[c] -= 1
        print(seen)
        return [k for k, v in seen.items() if v == -1][0]


# @lc code=end
