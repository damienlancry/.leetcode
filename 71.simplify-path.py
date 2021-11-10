#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = []
        for dir in path:
            if dir == "..":
                if stack:
                    stack.pop()
                else:
                    continue
            elif dir == ".":
                continue
            elif dir == "":
                continue
            else:
                stack.append(dir)
        return "/" + "/".join(stack)


# @lc code=end
