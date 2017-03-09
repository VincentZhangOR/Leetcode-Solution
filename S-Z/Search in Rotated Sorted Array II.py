# coding=utf-8
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        d = collections.defaultdict (lambda: -1)
        for i in xrange(len(nums)):
            d[nums[i]] = i
        return target in d
            
