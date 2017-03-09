# coding=utf-8
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res=0
        if x==0:
            return res
        s=str(abs(x))
        s=s[::-1]
        while s[0]=='0':
            s=s[1:]
        if x<0:
            s='-'+s
        res=int(s)
        if abs(res)>2147483647:
            res=0
        return res
