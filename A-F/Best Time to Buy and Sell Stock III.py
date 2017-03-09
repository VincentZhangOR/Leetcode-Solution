# coding=utf-8
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n <= 1:
            return 0
        ans = 0
        mi = float('inf')
        ma = 0
       
        s = collections.defaultdict (int)
        
        for k in xrange(n):
            if prices[k] < mi:
                mi = prices[k]
            s[0,k] = max(s[0,k-1], prices[k]-mi)
        
        for k in xrange(n-1,-1,-1):
            ma = max(ma, prices[k])
            s[k,n-1] = max(s[k+1,n-1], ma - prices[k])
                
        for k in xrange(n):
            temp = max(0,s[0,k])
            temp += max(0,s[k+1,n-1])
            ans = max(ans, temp)
        return ans
