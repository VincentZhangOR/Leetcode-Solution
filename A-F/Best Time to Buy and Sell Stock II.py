# coding=utf-8
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxprofit=0
        for i in xrange(len(prices)-1 ):
            if prices[i]<prices[i+1]:
                maxprofit+=prices[i+1] -prices[i]
        return maxprofit
        
