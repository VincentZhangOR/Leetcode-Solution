# coding=utf-8
class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        m = nums[len(nums)/2]
        return sum(abs(x - m) for x in nums)
