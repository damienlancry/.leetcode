#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    # brute force:
    # def uniquePaths(self, m: int, n: int) -> int:
    #     if m == 1 or n == 1:
    #         return 1
    #     return self.helper(m - 1, n - 1)

    # def helper(self, i, j):
    #     if i == 0 and j == 0:
    #         return 1
    #     if i == 0:
    #         return self.helper(i, j - 1)
    #     if j == 0:
    #         return self.helper(i - 1, j)
    #     ans = self.helper(i - 1, j) + self.helper(i, j - 1)
    #     return ans

    # dynamic programming: top down - memoization
    # def uniquePaths(self, m: int, n: int) -> int:
    #     if m == 1 or n == 1:
    #         return 1
    #     memo = [[None for _ in range(n)] for _ in range(m)]
    #     return self.helper(m - 1, n - 1, memo)

    # def helper(self, i, j, memo):
    #     if i == 0 and j == 0:
    #         return 1
    #     if memo[i][j] is None:
    #         if i == 0:
    #             memo[i][j] = self.helper(i, j - 1, memo)
    #         elif j == 0:
    #             memo[i][j] = self.helper(i - 1, j, memo)
    #         else:
    #             memo[i][j] = self.helper(i - 1, j, memo) + self.helper(i, j - 1, memo)
    #     return memo[i][j]

    # dynamic programming: bottom up - tabulation
    # def uniquePaths(self, m: int, n: int) -> int:
    #     dp = [[0 for i in range(n)] for j in range(m)]
    #     for i in range(m):
    #         dp[i][0] = 1
    #     for j in range(n):
    #         dp[0][j] = 1
    #     for i in range(1, m):
    #         for j in range(1, n):
    #             dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    #     return dp[-1][-1]

    # dynamic programming: bottom up - linear space
    # def uniquePaths(self, m: int, n: int) -> int:
    #     if m == 1 or n == 1:
    #         return 1
    #     dp = [0 for _ in range(n)]
    #     dp[0] = 0
    #     for _ in range(m):
    #         prev = 1
    #         for j in range(1, n):
    #             curr = prev + dp[j]
    #             dp[j] = curr
    #             prev = curr
    #     return dp[-1]


# @lc code=end
