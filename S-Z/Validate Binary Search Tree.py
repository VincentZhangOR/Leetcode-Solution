# coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if (not root.left) and (not root.right):
            return True
        elif not root.left:
            return (root.val<self .helpMin(root.right)) and self.isValidBST (root.right)
        elif not root.right:
            return (root.val>self .helpMax(root.left)) and self.isValidBST (root.left)
        else:
            return (root.val<self .helpMin(root.right)) and self.isValidBST (root.right) and (root .val>self.helpMax(root .left)) and self .isValidBST(root.left)
            
    def helpMax(self, root):
        if root==None:
            return None
        if root.right==None:
            return root.val
        else:
            return self.helpMax(root .right)
            
    def helpMin(self, root):
        if root==None:
            return None
        if root.left==None:
            return root.val
        else:
            return self.helpMin(root .left)
