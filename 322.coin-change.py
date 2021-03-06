#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf") for i in range(amount + 1)]
        dp[0] = 0
        for i in range(1, amount + 1):
            dp[i] = min(dp[i - coin] if i - coin >= 0 else float("inf") for coin in coins) + 1
        return dp[-1] if dp[-1] < float("inf") else -1


# @lc code=end
