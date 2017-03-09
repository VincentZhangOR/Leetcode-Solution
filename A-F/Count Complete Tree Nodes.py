# coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left=self.heightL(root)+1
        right=self.heightR(root)+1
        if left==right:
            return 2**(left)-1
        else:
            return 1+self.countNodes (root.left)+self .countNodes(root .right)
        
    def heightL(self, root):
        count=0
        while root.left:
            count+=1
            root=root.left
        return count
    
    def heightR(self, root):
        count=0
        while root.right:
            count+=1
            root=root.right

