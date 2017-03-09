# coding=utf-8
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in xrange(n):
            if nums[i] <= 0:
                nums[i] = n+2
        for i in xrange(n):
            if abs(nums[i]) <= n:
                nums[abs(nums[i])-1] = -abs(nums[abs (nums[i])-1])
        for i in xrange(n):
            if nums[i] > 0:
                return i+1
        return n+1
