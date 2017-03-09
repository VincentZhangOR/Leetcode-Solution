# coding=utf-8
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        i=0
        res=0
        maxLog=int(math.log(n)/math .log(5))
        num=0
        reduce=0
        while i<maxLog:
            mid=pow(5,maxLog-i)
            num=n/mid-reduce
            reduce+=num
            res+=num*(maxLog-i)
            i+=1
        return res
