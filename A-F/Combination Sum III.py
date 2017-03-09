# coding=utf-8
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        
        return self.dfs(k, n, 1, [], [])
        
    def dfs(self, k, n, start, ans, res):
        if k<0:
            return
        if n<0:
            return
        if n==0 and k==0:
            res.append(ans+[])
        for i in xrange(start, 10):
            ans.append(i)
            self.dfs(k-1, n-i, i+1, ans, res)
            ans.pop()
        return res
        
