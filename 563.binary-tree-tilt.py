#
# @lc app=leetcode id=563 lang=python3
#
# [563] Binary Tree Tilt
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.sum_tilt = 0

        def build_tilt_tree(root):
            if root.right and root.left:
                return TreeNode()
            if not root:
                return
            if not root.right and not root.left:
                return
            if not root.right:
                return build_tilt_tree(root.left)
            if not root.left:
                return build_tilt_tree(root.right)
            else:
                left_tilt = build_tilt_tree(root.left).val
                right_tilt = build_tilt_tree(root.right).val
                return abs(le)

        def helper(root, acc):
            if not root:
                return 0, acc
            if not root.right and not root.left:
                return 0, acc
            if not root.right:
                left_tilt, acc = helper(root.left, acc)
                root_tilt = abs(root.left.val) + left_tilt
                return root.left.val + left_tilt, acc + abs(helper(root.left.val))
            if not root.left:
                return acc + abs(root.right.val)
            else:
                tiltleft = self.findTilt(root.left)
                tiltright = self.findTilt(root.right)
            print(root.val, ti)
            return abs(root.left.val - root.right.val) + tiltleft + tiltright


# @lc code=end
