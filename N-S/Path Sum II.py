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
        :rtype: List[List[int]]
        """
        if root==None:
            return []
        return self.help(root, root .val, [root.val], [], sum)
        
        
    def help(self, root, cur, ans, res , sum):
        if root.left==None and root .right==None:
            if sum==cur:
                res.append(ans+[])
                return res
            else:
                return []
        if root.left!=None:
            self.help(root.left, cur +root.left.val, ans +[root.left.val], res ,sum)
        if root.right!=None:
            self.help(root.right, cur +root.right.val, ans +[root.right.val], res ,sum)
        return res
        
