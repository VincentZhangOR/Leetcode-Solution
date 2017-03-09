# coding=utf-8
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        s=[0]*(num+1)
        for i in xrange(1,len(s)):
            s[i]=s[i>>1]+(i&1)
        return s
