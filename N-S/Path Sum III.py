# coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        #if (not root.left) and (not root.right):
        #    return 1 if root.val == sum else 0
        return self.pathSum(root.left , sum) + self.pathSum(root .right, sum) + self.help (root, sum) 
        
    def help(self, root, sum):
        if not root:
            return 0
        res = 0
        if sum == root.val:
            res += 1
        #if (not root.left) and (not root.right):
        #    return 1 if root.val == sum else 0
        res += self.help(root.left, sum-root.val)+self.help (root.right,sum-root.val)
        return res
        
