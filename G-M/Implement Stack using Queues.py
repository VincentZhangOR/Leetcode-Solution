# coding=utf-8
class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue=[]
        self.size=0

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.queue.append(x)
        self.size+=1

    def pop(self):
        """
        :rtype: nothing
        """
        self.queue=self.queue[:self .size-1]
        self.size-=1

    def top(self):
        """
        :rtype: int
        """
        return self.queue[self.size-1]

    def empty(self):
        """
        :rtype: bool
        """
        if self.size==0:
            return True
        return False
