# coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if root == None:
            return res
        queue = [root]
        while queue:
            frontier = []
            temp = None
            for x in queue:
                if temp == None or x .val > temp:
                    temp = x.val
                if x.left:
                    frontier.append(x .left)
                if x.right:
                    frontier.append(x .right)
            if temp != None:
                res.append(temp)
            queue = frontier
        return res
