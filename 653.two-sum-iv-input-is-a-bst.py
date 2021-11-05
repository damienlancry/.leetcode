#
# @lc app=leetcode id=653 lang=python3
#
# [653] Two Sum IV - Input is a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        return dfs(root, set(), k)


def dfs(root, seen, target):
    if not root:
        return False
    if target - root.val in seen:
        return True
    seen.add(root.val)
    return dfs(root.left, seen, target) or dfs(root.right, seen, target)


# @lc code=end
