# coding=utf-8
class Solution(object):
    def countNumbersWithUniqueDigits (self, n):
        """
        :type n: int
        :rtype: int
        """
        res=1
        r=min(n,10)
        for i in xrange(1,r+1):
            res+=math.factorial(9 )/math.factorial(9-i )+math.factorial(9 )/math.factorial(9-i+1 )*(i-1)
        return res
