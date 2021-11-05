#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

# @lc code=start
def pprint(dp):
    print("\n".join([", ".join([str(int) for int in list]) for list in dp]))
    print()


class Solution:
    # brute force O(2^n)
    # def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    #     return self.helper(text1, text2, 0, 0)

    # def helper(self, s1, s2, i, j):
    #     if i == len(s1) or j == len(s2):
    #         return 0
    #     if s1[i] == s2[j]:
    #         return 1 + self.helper(s1, s2, i + 1, j + 1)
    #     else:
    #         return max(self.helper(s1, s2, i, j + 1), self.helper(s1, s2, i + 1, j))

    # dynamic programming: top down memoization
    # def longestCommonSubsequence(self, s1: str, s2: str) -> int:
    #     m = len(s1)
    #     n = len(s2)
    #     memo = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
    #     return self.helper(s1, s2, 0, 0, memo)

    # def helper(self, s1, s2, i, j, memo) -> int:
    #     if memo[i][j] < 0:
    #         if i == len(s1) or j == len(s2):
    #             memo[i][j] = 0
    #         elif s1[i] == s2[j]:
    #             memo[i][j] = 1 + self.helper(s1, s2, i + 1, j + 1, memo)
    #         else:
    #             memo[i][j] = max(
    #                 self.helper(s1, s2, i, j + 1, memo), self.helper(s1, s2, i + 1, j, memo)
    #             )
    #     return memo[i][j]

    # dynamic programming: bottom up tabulation
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)
        memo = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[m - i] == s2[n - j]:
                    memo[i][j] = 1 + memo[i - 1][j - 1]
                else:
                    memo[i][j] = max(memo[i - 1][j], memo[i][j - 1])
        return memo[m][n]


# @lc code=end
