# coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root==None:
            return []
        res=[[root.val]]
        queue=[root]
        while queue:
            front=[]
            mid=[]
            for x in queue:
                if x.left:
                    front.append(x .left)
                    mid.append(x.left .val)
                if x.right:
                    front.append(x .right)
                    mid.append(x.right .val)
            queue=front
            if mid!=[]:
                res=[mid]+res
        return res
