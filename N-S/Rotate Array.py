# coding=utf-8
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in -place instead.
        """
        
        for i in xrange(k):
            temp=nums.pop()
            nums.insert(0,temp)
