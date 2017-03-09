# coding=utf-8
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        d=[]
        for i in xrange(1,n+1):
            d.append(str(i))
        return self.dfs(d, [], [], k)

        
    def dfs(self, d, res, ans, k):
        if len(res)==k:
            return 
        if d==[] or d==None:
            res.append(''.join(ans))
            return
        f=math.factorial(len(d)-1)
        for i in xrange(abs((k-1)/f ),len(d)):
            ans.append(d[i])
            self.dfs(d[:i]+d[i+1:], res, ans, k-f*i)
            ans.pop()
        return res[-1]
