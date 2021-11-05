#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        ok = [True for _ in range(n + 1)]
        maxlen = max(len(word) for word in wordDict)
        words = set(wordDict)
        for i in range(len(s)):
            ok[i + 1] = any(
                ok[j] and s[j : i + 1] in words for j in range(i, max(0, i - maxlen) - 1, -1)
            )
        return ok[n]


# @lc code=end
