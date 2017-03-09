# coding=utf-8
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        n = max(x,y)
        ans = 0
        while n > 0:
            a = x%2
            b = y%2
            if a!=b:
                ans += 1
            x /=2
            y /=2
            n /=2
            #print 
        return ans
