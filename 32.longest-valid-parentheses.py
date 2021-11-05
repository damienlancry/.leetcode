#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return 0
        i = 0
        while i < n and s[i] == ")":
            i += 1
        j = n - 1
        while j >= 0 and s[j] == "(":
            j -= 1
        return helper(s[i : j + 1])


def pprint(dp):
    print("\n".join(str(d) for d in dp))


def helper(s):
    dp = [0] * (len(s) + 1)
    stack = []
    for i, c in enumerate(s):
        if c == "(":
            stack.append(i)
        else:
            if stack:
                p = stack.pop()
                dp[i + 1] = dp[p] + i - p + 1
    return max(dp)


# @lc code=end
