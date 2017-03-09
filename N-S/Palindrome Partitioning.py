# coding=utf-8
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        n=len(s)
        if n==0:
            return [[]]
        if n==1:
            return [[s]]
        return self.dfs(s, [], [])
        
        
    def isP(self, s):
        n=len(s)
        if n==0 or n==1:
            return True
        for i in xrange(n/2):
            if s[i]!=s[n-1-i]:
                return False
        return True
        
    def dfs(self, s, ans, res):
        n=len(s)
        if n==0:
            res.append(ans+[])
            return
        for i in xrange(n):
            if self.isP(s[:i+1] )==True:
                ans.append(s[:i+1])
                self.dfs(s[i+1:], ans, res)
                ans.pop()

