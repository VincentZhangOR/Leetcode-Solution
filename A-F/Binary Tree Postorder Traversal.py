# coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=[]
        if root==None:
            return res
        stack1=[]
        stack2=[]
        node=root
        stack1.append(node)
        while stack1:
            node=stack1.pop()
            if node.left:
                stack1.append(node .left)
            if node.right:
                stack1.append(node .right)
            stack2.append(node)
        while stack2:
            res.append(stack2.pop ().val)
        return res
            
            

