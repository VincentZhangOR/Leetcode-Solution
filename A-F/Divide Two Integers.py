# coding=utf-8
class Solution(object):
    def divide(self, dividend, divisor ):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor==0:
            return -1
        if dividend==0:
            return 0
        MAX_INT=0x7fffffff
        if (dividend>0 and divisor<0) or (dividend<0 and divisor >0):
            if abs(dividend)<abs (divisor):
                return 0
        a=abs(dividend)
        b=abs(divisor)
        sum=0
        count=0
        res=0
        while a>=b:
            sum=b
            count=1
            while sum+sum<=a:
                sum+=sum
                count+=count
            a-=sum
            res+=count
        if (dividend>0 and divisor<0) or (dividend<0 and divisor >0):
            res=0-res
        if res>MAX_INT:
            return MAX_INT
        return res
