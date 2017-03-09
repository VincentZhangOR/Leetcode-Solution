# coding=utf-8
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=nums[0]
        cur=0
        #nums=nums[1:]
        for x in nums:
            cur+=x
            res=max(cur,res)
            if cur<0:
                cur=0
        return res
