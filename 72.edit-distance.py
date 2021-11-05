#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start
class Solution:
    # brute force O(3^n)
    # def minDistance(self, word1: str, word2: str) -> int:
    #     def dp(i, j):
    #         if i >= len(word1) or j >= len(word2):
    #             ans = abs(len(word1) - i - len(word2) + j)
    #         elif word1[i] == word2[j]:
    #             ans = dp(i + 1, j + 1)
    #         else:
    #             insert = dp(i, j + 1)
    #             delete = dp(i + 1, j)
    #             replace = dp(i + 1, j + 1)
    #             ans = min(insert, delete, replace) + 1
    #         return ans

    #     return dp(0, 0)

    # dynamic programming: top down - memoization
    # def minDistance(self, word1: str, word2: str) -> int:
    #     def dp(i, j):
    #         if (i, j) in memo:
    #             return memo[(i, j)]
    #         elif i >= len(word1) or j >= len(word2):
    #             memo[(i, j)] = abs(len(word1) - i - len(word2) + j)
    #         elif word1[i] == word2[j]:
    #             memo[(i, j)] = dp(i + 1, j + 1)
    #         else:
    #             insert = dp(i, j + 1)
    #             delete = dp(i + 1, j)
    #             replace = dp(i + 1, j + 1)
    #             memo[(i, j)] = min(insert, delete, replace) + 1
    #         return memo[(i, j)]

    #     memo = dict()
    #     return dp(0, 0)

    # dynamic programing: bottom up - tabulation
    # def minDistance(self, word1: str, word2: str) -> int:
    #     m = len(word1)
    #     n = len(word2)
    #     dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    #     for i in range(m + 1):
    #         dp[i][0] = i
    #     for j in range(n + 1):
    #         dp[0][j] = j
    #     for i in range(1, m + 1):
    #         for j in range(1, n + 1):
    #             if word1[i - 1] == word2[j - 1]:
    #                 dp[i][j] = dp[i - 1][j - 1]
    #             else:
    #                 dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
    #     return dp[m][n]


# @lc code=end
