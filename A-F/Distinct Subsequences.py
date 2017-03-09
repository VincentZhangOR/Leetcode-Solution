# coding=utf-8
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        d = collections.defaultdict (int)
        
        lt = len(t)
        tset = set(t)
        news = []
        for x in s:
            if x in tset:
                news.append(x)
        ls = len(news)
        for i in xrange(ls):
            d[i,0] = d[i-1,0] + 1 if news[i]==t[0] else d[i -1,0]
            for j in xrange(1,min(lt,i +1)):
                d[i,j] = d[i-1,j-1] + d[i-1,j] if news[i] == t[j] else d[i-1 ,j]
                #print i,j,d
        return d[ls-1,lt-1]
                
