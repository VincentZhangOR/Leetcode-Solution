# coding=utf-8
class Solution(object):
    def coinChange(self, coins, amount ):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp=[0]+[-1]*amount
        for i in xrange(amount):
            if dp[i]<0:
                continue
            for x in coins:
                if x+i>amount:
                    continue
                if dp[x+i]<0 or dp[x +i]>dp[i]+1:
                    dp[x+i]=dp[i]+1
        return dp[amount]
