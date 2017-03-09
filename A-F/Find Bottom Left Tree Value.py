# coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root ):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return None
        queue = [root]
        res = root.val
        while queue:
            frontier = []
            flag = 0
            for x in queue:
                if flag == 0:
                    res = x.val
                    flag = 1
                if x.left:
                    frontier.append(x .left)
                if x.right:
                    frontier.append(x .right)
                queue = frontier
        return res
