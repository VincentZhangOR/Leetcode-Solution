# coding=utf-8
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d={}
        for i in xrange(len(nums)):
            if nums[i] not in d:
                diff=target-nums[i]
                d[diff]=i
            else:
                return [d[nums[i]],i]
        return None
            
