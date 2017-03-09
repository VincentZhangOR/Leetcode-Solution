# coding=utf-8
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in -place instead.
        """
        if len(nums)<=1:
            return
        partition=-1
        for i in xrange(len(nums)-2 ,-1,-1):
            if nums[i]<nums[i+1]:
                partition=i
                break
        #print partition
        if partition==-1:
            nums.reverse()
            return
        for j in xrange(len(nums)-1 ,partition,-1):
            if nums[j] >nums[partition]:
                nums[j] ,nums[partition] =nums[partition] ,nums[j]
                break
        nums[partition+1:len(nums)] =nums[partition+1:len
