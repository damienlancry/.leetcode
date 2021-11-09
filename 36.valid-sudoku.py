#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
def pprint(board):
    for row in board:
        print(row)


class Solution:
    def isValidRow(self, row):
        seen = set()
        for i in range(len(row)):
            if row[i] == ".":
                continue
            if row[i] in seen:
                return False
            seen.add(row[i])
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        pprint(board)
        for i in range(len(board)):
            if not self.isValidRow(board[i]):
                print("row", i)
                return False
        for i in range(len(board[0])):
            column = [row[i] for row in board]
            if not self.isValidRow(column):
                print("column", i)
                return False
        for i in range(0, len(board), 3):
            for j in range(0, len(board[0]), 3):
                square = [
                    board[i][j],
                    board[i][j + 1],
                    board[i][j + 2],
                    board[i + 1][j],
                    board[i + 1][j + 1],
                    board[i + 1][j + 2],
                    board[i + 2][j],
                    board[i + 2][j + 1],
                    board[i + 2][j + 2],
                ]
                if i == j == 0:
                    print("square", square)

                if not self.isValidRow(square):
                    print("square", i, j)
                    return False
        return True


# @lc code=end
