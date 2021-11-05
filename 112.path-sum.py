#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#
# https://leetcode.com/problems/path-sum/description/
#
# algorithms
# Easy (42.79%)
# Likes:    3101
# Dislikes: 610
# Total Accepted:    614.8K
# Total Submissions: 1.4M
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,null,1]\n22'
#
# Given the root of a binary tree and an integer targetSum, return true if the
# tree has a root-to-leaf path such that adding up all the values along the
# path equals targetSum.
#
# A leaf is a node with no children.
#
#
# Example 1:
#
#
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# Output: true
#
#
# Example 2:
#
#
# Input: root = [1,2,3], targetSum = 5
# Output: false
#
#
# Example 3:
#
#
# Input: root = [1,2], targetSum = 0
# Output: false
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000
#
#
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        if not root.right and not root.left and root.val == targetSum:
            return True
        targetSum -= root.val
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

        # def helper(root: TreeNode, targetSum: int) -> bool:
        #     if not root.right and not root.left:
        #         return targetSum == root.val
        #     if not root.right:
        #         return helper(root.left, targetSum - root.val)
        #     if not root.left:
        #         return helper(root.right, targetSum - root.val)
        #     return helper(root.left, targetSum - root.val) or helper(
        #         root.right, targetSum - root.val
        #     )

        # return helper(root, targetSum) if root else False


# @lc code=end
