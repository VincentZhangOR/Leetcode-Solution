# coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in -place instead.
        """
        ans=[]
        ansp=[]
        self.inorder(root, ans, ansp )
        ans.sort()
        for i in xrange(len(ans)):
            ansp[i].val=ans[i]
        
    def inorder(self, root, ans, ansp):
        if root:
            self.inorder(root.left, ans, ansp)
            ans.append(root.val)
            ansp.append(root)
            self.inorder(root.right, 
