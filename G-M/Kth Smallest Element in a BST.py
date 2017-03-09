# coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        leftsize=self.size(root.left)
        if leftsize>=k:
            return self.kthSmallest (root.left,k)
        elif leftsize==k-1:
            return root.val
        else:
            return self.kthSmallest (root.right,k-1 -leftsize)
        
    
    def size(self, root):
        if not root:
            return 0
        return self.size(root.left)+1 +self.size(root.right)
        
