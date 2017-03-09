# coding=utf-8
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        d={}
        for x in s:
            if x not in d:
                d[x]=1
            else:
                d[x]+=1
        for y in t:
            if y not in d:
                return y
            else:
                d[y]-=1
                if d[y]==0:
                    del d[y]
