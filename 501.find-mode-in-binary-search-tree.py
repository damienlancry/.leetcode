#
# @lc app=leetcode id=501 lang=python3
#
# [501] Find Mode in Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def helper(root: Optional[TreeNode]) -> List[int]:

            if not root:
                return [], 0

            if not root.left and not root.right:
                return [root.val], 1

            modeleft, freqleft = helper(root.left)
            moderight, freqright = helper(root.right)

            assert freqleft > 0 or freqright > 0, "at least one of those should be nonzero"

            if root.val in modeleft:
                modeleft, freqleft = [root.val], freqleft + 1
            if root.val in moderight:
                moderight, freqright = [root.val], freqright + 1
            # if root.val in moderight or modeleft now freqleft and freqright are greater than one

            if freqright > freqleft:
                if freqright == 1:
                    return moderight + [root.val], 1
                else:
                    return moderight, freqright
            elif freqleft > freqright:
                if freqleft == 1:
                    return modeleft + [root.val], 1
                else:
                    return modeleft, freqleft
            elif freqleft == freqright == 1:
                return list(set(modeleft + moderight + [root.val])), freqleft
            else:
                return list(set(modeleft + moderight)), freqleft

        mode, _ = helper(root)
        return mode


# @lc code=end
