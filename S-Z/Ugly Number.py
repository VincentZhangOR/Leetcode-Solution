# coding=utf-8
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        d={1,2,3,4,5,6,8,9,10}
        if num<=0:
            return False
        
        elif num in d:
            return True
        
        if num%2==0:
            return self.isUgly(num/2)
        elif num%3==0:
            return self.isUgly(num/3)
        elif num%5==0:
            return self.isUgly(num/5)
        return False
