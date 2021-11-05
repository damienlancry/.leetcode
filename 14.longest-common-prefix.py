#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        i = 0
        minlen = min([len(s) for s in strs])
        if minlen == 0:
            return res
        if len(strs) == 1:
            return strs[0]

        while len(res) < minlen:
            res += strs[0][i]
            i += 1
            if not all([s.startswith(res) for s in strs]):
                return res[:-1]
        return res


# @lc code=end
