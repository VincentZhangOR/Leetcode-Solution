# coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.construct(preorder , inorder, 0,len(preorder ),0,len(inorder))
        
    
    def construct(self, preorder, inorder, preStart, preEnd, inStart, inEnd):
        if preStart>=preEnd:
            return None
        root=TreeNode (preorder[preStart])
        i=inorder[inStart:inEnd].index (preorder[preStart])
        root.left=self.construct (preorder, inorder ,preStart+1,preStart+i+1 ,inStart,inStart+i)
        root.right=self.construct (preorder, inorder ,preStart+i+1,preEnd ,inStart+i+1,inEnd)
        return root
