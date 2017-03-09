# coding=utf-8
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        dp = collections.defaultdict (int)
        dn = collections.defaultdict (int)
        res = nums[0]
        if nums[0] > 0:
            dp[0] = nums[0]
        elif nums[0] < 0:
            dn[0] = nums[0]
        for i in xrange(1,len(nums)):
            if nums[i] > 0:
                dp[i] = max(dp[i-1] * nums[i], nums[i])
                dn[i] = dn[i-1] * nums[i]
            elif nums[i] < 0:
                dp[i] = dn[i-1] * nums[i]
                dn[i] = min(dp[i-1] * nums[i], nums[i])
            if dp[i] > res:
                res = dp[i]
        return res
