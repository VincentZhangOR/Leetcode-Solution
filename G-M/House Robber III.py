# coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root)[0]
        
    def dfs(self, root):
        if not root:
            return 0, 0
        L, noL = self.dfs(root.left)
        R, noR = self.dfs(root.right)
        return max(root.val+noL+noR, L +R), L+R
