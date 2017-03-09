# coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=[]
        if root==None:
            return res
        #res.append(root.val)
        queue=[root]
        while queue!=[]:
            res.append(queue[0].val)
            frontier=[]
            for x in queue:
                if x.right!=None:
                    frontier.append(x .right)
                if x.left!=None:
                    frontier.append(x .left)
            queue=frontier
        return res
