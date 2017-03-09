# coding=utf-8
# Definition for a binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack=[]
        self.push(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.stack==[]:
            return False
        else:
            return True

    def next(self):
        """
        :rtype: int
        """
        if self.stack==[]:
            return None
        top=self.stack.pop()
        self.push(top.right)
        return top.val
            
    def push(self,root):
        while root:
            self.stack.append(root)
            root=root.left
        
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next
