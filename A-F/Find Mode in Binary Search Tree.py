# coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        left = self.findMode(root .left)
        right = self.findMode(root .right)
        nl, nr = 0, 0
        if left != []:
            nl = self.findK(root .left, left[0])
        if right != []:
            nr = self.findK(root .right, right[0])
        nroot = self.findK(root, root.val)
        if nl == nr:
            if nroot > nl:
                return [root.val]
            elif nroot == nl:
                return [root.val] + left + right
            else:
                return left + right
        elif nl > nr:
            if nroot > nl:
                return [root.val]
            elif nroot == nl:
                return [root.val] + left
            else:
                return left
        else:
            if nroot > nr:
                return [root.val]
            elif nroot == nr:
                return [root.val] + right
            else:
                return right
            
                
    def findK(self, root, k):
        if root == None:
            return 0
        if root.val == k:
            return 1 + self.findK (root.left,k) + self .findK(root.right,k)
        if root.val < k:
            return self.findK(root .right,k)
        else:
            return self.findK(root
