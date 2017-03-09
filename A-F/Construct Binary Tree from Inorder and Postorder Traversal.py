# coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        #if not inorder:
        #    return None
        self.inorder=inorder
        self.postorder=postorder
        return self.help(0, 0, len (inorder))
        
        
    def help(self, inLeft, postLeft, Len):
        if Len<=0:
            return None
        root=TreeNode(self .postorder[postLeft+Len -1])
        index=self.inorder.index (self.postorder[postLeft +Len-1])
        root.left=self.help(inLeft, postLeft, index-inLeft)
        root.right=self.help(index+1 , postLeft+index-inLeft, 
