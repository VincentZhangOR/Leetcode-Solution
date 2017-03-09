# coding=utf-8
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp=[0]*(target+1)
        dp[0]=1
        for i in xrange(target+1):
            for x in nums:
                if i>=x:
                    dp[i]+=dp[i-x]
        return dp[target]
