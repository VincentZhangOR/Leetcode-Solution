# coding=utf-8
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        n=len(s)
        ans=[False]*(n+1)
        ans[0]=True
        for i in xrange(1,n+1):
            for j in xrange(i):
                if ans[j] and s[j:i] in wordDict:
                    ans[i]=True
                    break
        return ans[n]
            
