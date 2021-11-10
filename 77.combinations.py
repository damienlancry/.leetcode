#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret = []
        self.dfs(n, k, 0, [], ret)
        return ret

    def dfs(self, n, k, index, path, ret):
        if len(path) == k:
            ret.append(path)
            return
        for i in range(index + 1, n + 1):
            if i in path:
                continue
            self.dfs(n, k, i, path + [i], ret)


# @lc code=end
