# coding=utf-8
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        d=set()
        #d.add()
        sum=n
        digit=0
        while sum not in d:
            d.add(sum)
            n=sum
            sum=0
            while n>0:
                digit=n%10
                sum+=digit*digit
                n/=10
                #print sum
            if sum==1:
                return True
        return False
