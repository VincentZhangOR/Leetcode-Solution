# coding=utf-8
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        x=n
        i=0
        while x!=0:
            x = x & (x-1)
            i+=1
            
        return i
