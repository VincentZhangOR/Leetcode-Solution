# coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        return self.bfs(root)
        
    def bfs(self, root):
        if root==None:
            return []
        queue=[root]
        count=1
        res=[]
        while queue!=[]:
            cur=[]
            frontier=[]
            queue=queue[::-1]
            for x in queue:
                cur.append(x.val)
                if count%2==1:
                    if x.left!=None:
                        frontier .append(x.left)
                    if x.right!=None:
                        frontier .append(x.right)
                else:
                    if x.right!=None:
                        frontier .append(x.right)
                    if x.left!=None:
                        frontier .append(x.left) 
            res.append(cur)
            queue=frontier
            count+=1
            print count
        return res
                    
