#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        if not root.left and not root.right:
            return [f"{root.val}"]
        left_paths = [f"{root.val}->" + path for path in self.binaryTreePaths(root.left)]
        right_paths = [f"{root.val}->" + path for path in self.binaryTreePaths(root.right)]
        return left_paths + right_paths


# @lc code=end
