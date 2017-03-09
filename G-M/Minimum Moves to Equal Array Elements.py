# coding=utf-8
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        count = 0
        m = nums[0]
        for i in xrange(n):
            count += nums[i]
            if nums[i] < m:
                m = nums[i]
        return count-n*m
