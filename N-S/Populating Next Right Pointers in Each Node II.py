# coding=utf-8
# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root:
            return
        queue=[root]
        while queue!=[]:
            frontier=[]
            for i in xrange(len(queue )):
                if i<len(queue)-1:
                    queue[i].next =queue[i+1]
                if queue[i].left:
                    frontier.append (queue[i].left)
                if queue[i].right:
                    frontier.append (queue[i].right)
            queue=frontier
