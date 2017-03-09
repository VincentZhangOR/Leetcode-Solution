# coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in -place instead.
        """
        if not root:
            return
        elif not root.left and not root.right:
            return
        elif not root.right:
            self.flatten(root.left)
            root.right=root.left
            root.left=None
        elif not root.left:
            self.flatten(root.right)
        else:
            self.flatten(root.left)
            self.flatten(root.right)
            temp=root.right
            root.right=root.left
            cur=root.left
            while cur and cur.right:
                cur=cur.right
            cur.right=temp
            root.left=None
