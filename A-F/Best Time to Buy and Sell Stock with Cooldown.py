# coding=utf-8
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n < 2:
            return 0
        d = collections.defaultdict (int)
        #d[1] = max(0, prices[1] - prices[0])
        for i in xrange(1, n):
            temp = max(d[k] + prices[i] - prices[k +2] for k in range(-2 ,i-2))
            d[i] = max(temp, d[i-1])
        return d[n-1]
