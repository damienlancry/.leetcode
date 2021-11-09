#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        dp = "1"
        for _ in range(2, n + 1):
            start = 0
            finish = 1
            new = ""
            while finish < len(dp):
                while finish < len(dp) and dp[finish] == dp[start]:
                    finish += 1
                new += str(finish - start) + dp[start]
                start = finish
            if start < len(dp):
                new += str(finish - start) + dp[start]
            dp = new
        return dp


# @lc code=end
