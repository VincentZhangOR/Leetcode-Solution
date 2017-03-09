# coding=utf-8
class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        start=diff=1
        count=0
        while n>1:
            diff *= 2
            n /= 2
            count+=1
            if count % 2:
                start += diff/2 + diff * (n-1)
            else:
                start -= diff/2 + diff * (n-1)
        return start
        
