# coding=utf-8
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d={}
        l=[]
        n=len(s)
        if n==0:
            return -1
        for i in xrange(n):
            if s[i] not in d:
                d[s[i]]=i
                l.append(i)
            else:
                if d[s[i]]==-1:
                    continue
                else:
                    l.remove(d[s[i]])
                    d[s[i]]=-1
        if len(l)==0:
            return -1
        return l[0]
