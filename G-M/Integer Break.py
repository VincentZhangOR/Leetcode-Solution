# coding=utf-8
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=3:
            if n==2:
                return 1
            else:
                return 2
        if n%3==0:
            return pow(3,n/3)
        elif n%3==1:
            return pow(3,n/3-1)*4
        else:
            return pow(3,n/3)*2
            
