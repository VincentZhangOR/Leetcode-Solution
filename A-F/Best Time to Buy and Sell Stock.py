# coding=utf-8
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices==[]:
            return 0
        low = prices[0]
        maxprofit=0
        for i in xrange(len(prices)):
            low=min(prices[i],low)
            maxprofit=max(prices[i] -low,maxprofit)
        return maxprofit
