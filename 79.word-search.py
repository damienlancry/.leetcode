#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

from typing import List


# @lc code=start
def pprint(board):
    for row in board:
        print(row)


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(k, path):
            if k == len(word):
                return True
            i, j = path[-1]
            if i + 1 < m and (i + 1, j) not in path and board[i + 1][j] == word[k]:
                if dfs(k + 1, path + [(i + 1, j)]):
                    return True
            if i - 1 >= 0 and (i - 1, j) not in path and board[i - 1][j] == word[k]:
                if dfs(k + 1, path + [(i - 1, j)]):
                    return True
            if j + 1 < n and (i, j + 1) not in path and board[i][j + 1] == word[k]:
                if dfs(k + 1, path + [(i, j + 1)]):
                    return True
            if j - 1 >= 0 and (i, j - 1) not in path and board[i][j - 1] == word[k]:
                if dfs(k + 1, path + [(i, j - 1)]):
                    return True
            return False

        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(1, [(i, j)]):
                        return True

        return False


Solution().exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB")
Solution().exist([["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]], "AAB")
Solution().exist([["a", "b"], ["c", "d"]], "cdba")
# @lc code=end
