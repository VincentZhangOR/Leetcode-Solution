# coding=utf-8
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=b=c=None
        for x in nums:
            if x>a:
                a,b,c=x,a,b
            elif a>x>b:
                b,c=x,b
            elif b>x>c:
                c=x
        return c if c!=None else a
                
