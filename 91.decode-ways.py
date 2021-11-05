#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    # brute force
    # def numDecodings(self, s: str) -> int:
    #     return self.helper(s, 0)

    # def helper(self, s, i):
    #     n = len(s)
    #     if i == n:
    #         return 1
    #     if s[i] == "0":
    #         return 0
    #     ans = self.helper(s, i + 1)
    #     if i < n - 1 and (s[i] == "1" or s[i] == "2" and s[i + 1] < "7"):
    #         ans += self.helper(s, i + 2)
    #     return ans

    # dynamic programming: top down - memoization
    # def numDecodings(self, s: str) -> int:
    #     memo = [None for i in range(len(s) + 1)]
    #     return self.helper(s, 0, memo)

    # def helper(self, s, i, memo):
    #     n = len(s)
    #     if i == n:
    #         return 1
    #     if memo[i] is None:
    #         if s[i] == "0":
    #             memo[i] = 0
    #         else:
    #             ans = self.helper(s, i + 1, memo)
    #             if i < n - 1 and (s[i] == "1" or s[i] == "2" and s[i + 1] < "7"):
    #                 ans += self.helper(s, i + 2, memo)
    #             memo[i] = ans
    #     return memo[i]

    # dynamic programming: top down - memoization
    # def numDecodings(self, s: str) -> int:
    #     if int(s[0]) == 0:
    #         return 0
    #     n = len(s)
    #     dp = [0 for _ in range(n + 1)]
    #     dp[n] = 1
    #     for i in range(n - 1, -1, -1):
    #         if s[i] == "0":
    #             continue

    #         dp[i] = dp[i + 1]
    #         if i < n - 1 and (s[i] == "1" or s[i] == "2" and s[i + 1] < "7"):
    #             dp[i] += dp[i + 2]
    #     return dp[0]

    # dynamic programming: top down - two variables
    def numDecodings(self, s: str) -> int:
        if int(s[0]) == 0:
            return 0
        n = len(s)
        prev = 0
        curr = 1
        for i in range(n - 1, -1, -1):
            if s[i] == "0":
                curr, prev = 0, curr
            elif i < n - 1 and (s[i] == "1" or s[i] == "2" and s[i + 1] < "7"):
                curr, prev = curr + prev, curr
            else:
                curr, prev = curr, curr
        return curr


# @lc code=end
