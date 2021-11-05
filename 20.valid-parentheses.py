#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
valid = ["()", "{}", "[]"]


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == "{" or c == "(" or c == "[":
                stack.append(c)
            elif not stack:
                return False
            else:
                top = stack.pop()
                if not top + c in valid:
                    return False
        return len(stack) == 0


# @lc code=end
