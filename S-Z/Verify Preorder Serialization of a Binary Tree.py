# coding=utf-8
class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        if preorder == '#':
            return True
        nodes = preorder.split(',')
        stack = []
        #if nodes[0] == '#':
        #    return False
        #stack = [nodes[0]]
        for i in xrange(len(nodes)):
            if nodes[i] == '#':
                if stack == []:
                    return False
                elif stack[-1] == '#':
                    while stack[-1] == '#':
                        stack.pop()
                        stack.pop()
                        if stack == []:
                            return True if i == len (nodes)-1 else False
                    stack.append('#' )
                else: 
                    stack.append('#'
