# coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n==0:
            return []
        return self.dfs(1,n)
        
    def dfs(self, start, end):
        if start>end:
            return [None]
        res=[]
        for x in xrange(start, end+1):
            left=self.dfs(start,x-1)
            right=self.dfs(x+1,end)
            for i in left:
                for j in right:
                    root=TreeNode(x)
                    root.left=i
                    root.right=j
                    res.append(root)
        return res
                    
