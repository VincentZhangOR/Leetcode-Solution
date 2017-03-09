# coding=utf-8
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = []
        for x in nums:
            nums[abs(x)-1] = -abs (nums[abs(x)-1]) 
        for i in xrange(n):
            nums[abs(nums[i])-1] = -(nums[abs(nums[i])-1] )
        for i in xrange(n):
            if nums[i] < 0:
                res.append(i+1)
        return res
