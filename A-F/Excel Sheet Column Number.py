# coding=utf-8
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        mmm ='ABCDEFGHIJKLMNOPQRSTUVWX YZ'
        d={}
        i=1
        for x in mmm:
            d[x]=i
            i+=1
        #s=s[::-1]
        l=len(s)-1
        res=0
        for y in s:
            res+=d[y]*pow(26,l)
            l-=1
        return res
