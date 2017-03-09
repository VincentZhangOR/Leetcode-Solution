# coding=utf-8
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        s='ZABCDEFGHIJKLMNOPQRSTUVWXY'
        d={}
        for i in xrange(0,26):
            d[i]=s[i]
        res=''
        #n=n-1
        while n>0:
            mid=n%26
            #if mid==0:
                
            res=d[mid]+res
            #if n==26:
            #    break
            n=(n-1)/26
            #n=n-1
            
        return res
