#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ret = []

        def dfs(index, path):
            if len(path) == 4:
                if index == len(s):
                    ret.append(".".join(path))
                else:
                    return
            if index < len(s):
                dfs(index + 1, path + [s[index]])
            if index < len(s) - 1 and s[index] != "0":
                dfs(index + 2, path + [s[index : index + 2]])
            if index < len(s) - 2 and s[index] != "0" and int(s[index : index + 3]) < 256:
                dfs(index + 3, path + [s[index : index + 3]])

        dfs(0, [])
        return ret


# @lc code=end
