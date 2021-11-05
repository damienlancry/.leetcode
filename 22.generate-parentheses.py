#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]
        acc = ["()"]
        for i in range(1, n):
            next = set()
            for element in acc:
                for i in range(len(element)):
                    next.add(element[:i] + "()" + element[i:])
            acc = list(next)
        return acc


# @lc code=end
