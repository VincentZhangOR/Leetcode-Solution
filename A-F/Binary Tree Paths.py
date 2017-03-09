# coding=utf-8
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        from collections import deque
        if root is None:
            return []
        queue = deque( [ [root, str (root.val)] ] )
        ans = []
        while queue:
            front, path = queue .popleft()
            if front.left is None and front.right is None:
                ans += path,
                continue
            if front.left:
                queue += [front.left, path + "->" + str (front.left.val)],
            if front.right:
                queue += [front.right, path + "->" + str (front.right.val)],
        return ans
