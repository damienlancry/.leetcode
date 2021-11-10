#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#


# @lc code=start
def pprint(dp):
    for row in dp:
        print(row)


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[m - 1][n - 1] = 1 if obstacleGrid[m - 1][n - 1] == 0 else 0
        for j in range(n - 2, -1, -1):
            dp[m - 1][j] = 1 if dp[m - 1][j + 1] == 1 and obstacleGrid[m - 1][j] == 0 else 0
        for i in range(m - 2, -1, -1):
            dp[i][n - 1] = 1 if dp[i + 1][n - 1] == 1 and obstacleGrid[i][n - 1] == 0 else 0
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
        return dp[0][0]


# @lc code=end
