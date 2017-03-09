# coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.help(root, 0)
        
    def help(self, root, presum):
        if not root:
            return 0
        presum=presum*10+root.val
        if root.left==None and root .right==None:
            return presum
        return self.help(root.left, presum)+self.help(root .right, presum)
