# coding=utf-8
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length=len(nums)
        if length==0:
            return 0
        if length==1:
            return nums[0]
        if length==2:
            return max(nums[0],nums[1] )
        i=3
        d={0:0,1:nums[0],2:max(nums[0] ,nums[1])}
        while i<=length:
            
            d[i]=max(d[i-2]+nums[i-1] ,d[i-1])
            i+=1
        
        return d[length]
