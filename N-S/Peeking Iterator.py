# coding=utf-8
# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iter = iterator
        #self.flag = False
        #self.nextEle = None
        self.cur = iterator.next() if iterator.hasNext() else None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.cur
        

    def next(self):
        """
        :rtype: int
        """
        temp = self.cur
        if self.iter.hasNext():
            self.cur = self.iter .next()
        else:
            self.cur = None
        return temp
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.cur) or self.iter.hasNext()

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator (nums))
# while iter.hasNext():
#     val = iter.peek() # Get the 
