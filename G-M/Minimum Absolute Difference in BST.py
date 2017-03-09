# coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def leftmost(r):
            if r.left == None:
                return r.val
            return leftmost(r.left)
            
        def rightmost(r):
            if r.right == None:
                return r.val
            return rightmost(r.right)
        
        if root.left == None and root .right == None:
            return float('inf')
        if root.left == None:
            return min(abs(root.val - leftmost(root.right)), abs(self .getMinimumDifference (root.right)))
        if root.right == None:
            return min(abs(root.val - rightmost(root.left)), abs(self .getMinimumDifference (root.left)))
        return min(abs(root.val - leftmost(root.right)), abs (self.getMinimumDifference (root.right)), abs(root .val - rightmost(root.left )), abs(self .getMinimumDifference(root .left)))
            
            
