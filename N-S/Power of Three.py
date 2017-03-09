# coding=utf-8
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<1:
            return False
        #maxValue=0x7fffffff
        #maxPower=int(pow(3,int(math .log(maxValue)/math.log(3 ))))
        #print maxPower
        if 1162261467%n==0:
            return True
        return False
