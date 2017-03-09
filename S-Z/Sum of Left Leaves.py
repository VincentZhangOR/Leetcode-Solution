# coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None or (root.left ==None and root.right ==None):
            return 0
        if root.left==None:
            return self .sumOfLeftLeaves (root.right)
        #if root.right==None:
        #    return self .sumOfLeftLeaves(root .left)
        if root.left.left==None and root.left.right==None:
            return root.left.val +self .sumOfLeftLeaves (root.right)
        else:
            return self
