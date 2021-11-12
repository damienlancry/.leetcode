#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#

from typing import List, Optional


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, i):
        if i == self.val:
            raise ValueError(f"cannot insert value {i} because value already in tree")
        elif i < self.val and self.left:
            self.left.insert(i)
        elif i < self.val:
            self.left = TreeNode(i)
        elif self.right:
            self.right.insert(i)
        else:
            self.right = TreeNode(i)

    def remove(self, i):
        if i == self.val:
            raise ValueError("value to be removed should not be root")
        elif i < self.val and i == self.left.val:
            self.left = None
        elif i > self.val and i == self.right.val:
            self.right = None
        elif i < self.val:
            self.left.remove(i)
        else:
            self.right.remove(i)

    def __str__(self):
        ans = []

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            ans.append(root.val)
            dfs(root.right)

        dfs(self)
        print(ans)

    def __repr__(self) -> str:
        ans = []

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            ans.append(root.val)
            dfs(root.right)

        dfs(self)
        print(ans)


def insert(i, tree):
    if not tree:
        return TreeNode(i)
    elif i == tree.val:
        raise ValueError(f"cannot insert value {i} because value already in tree")
    elif i < tree.val:
        tree.left = insert(i, tree.left)
        return tree
    else:
        tree.right = insert(i, tree.right)
        return tree


def clone(root):
    if not root:
        return None
    copy = TreeNode(root.val)
    copy.left = clone(root.left)
    copy.right = clone(root.right)
    return copy


def isin(tree, trees):
    for copy in trees:
        if iscopy(tree, copy):
            return True
    return False


def iscopy(root, othr):
    if not root and not othr:
        return True
    if not root or not othr:
        return False
    return root.val == othr.val and iscopy(root.left, othr.left) and iscopy(root.right, othr.right)


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        ans = []
        seen = set()

        def dfs(size, tree):
            if size == n:
                print(size)
                if not isin(tree, ans):
                    ans.append(tree)
                return
            for i in range(1, n + 1):
                if i not in seen:
                    seen.add(i)
                    itree = clone(tree)
                    itree = insert(i, itree)
                    dfs(size + 1, itree)
                    seen.remove(i)

        dfs(0, None)
        return ans


Solution().generateTrees(3)

# @lc code=end
