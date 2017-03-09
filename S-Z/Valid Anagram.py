# coding=utf-8
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        d={}
        for x in s:
            if x not in d:
                d[x]=1
            else:
                d[x]+=1
        for y in t:
            if y not in d or d[y]==0:
                return False
            else:
                d[y]-=1
        return True
