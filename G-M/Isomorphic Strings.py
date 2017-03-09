# coding=utf-8
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        d={}
        m=set()
        for x,y in zip(s,t):
            if x not in d:
                d[x]=y
                m.add(y)
            else:
                if d[x]!=y:
                    return False
        if len(d)!=len(m):
            return False
        return True
        
