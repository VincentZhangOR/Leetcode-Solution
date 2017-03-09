# coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root==None:
            return []
        queue=[root]
        res=[]
        res.append([root.val])
        #print res
        while queue!=[]:
            frontier=[]
            value=[]
            while queue!=[]:
                cur=queue[0]
                del queue[0]
                if cur.left!=None:
                    frontier.append (cur.left)
                    value.append(cur .left.val)
                if cur.right!=None:
                    frontier.append (cur.right)
                    value.append(cur .right.val)
            queue=frontier
            if value!=[]:
                res.append(value)
        return res
            
