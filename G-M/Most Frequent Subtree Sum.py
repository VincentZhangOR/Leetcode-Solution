# coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root ):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        d = collections.defaultdict (int)
        s = collections.defaultdict (int)
        
        def topdown(r):
            if r in d:
                return d[r]
            if r == None:
                #d[r] = 0
                return 0
            d[r] = r.val + topdown(r .left) + topdown(r .right)
            return d[r]
        
        topdown(root)
        for x in d:
            s[d[x]] += 1
        #print d, s
        temp = max(s[x] for x in s)
        return [x for x in s if s[x] == temp]
        
