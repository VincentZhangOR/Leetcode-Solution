# coding=utf-8
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length=len(nums)
        if length==1:
            return nums[0]
        if length==2:
            return min(nums[0],nums[1] )
        left=0
        right=len(nums)-1
        mid=(left+right)/2
        if nums[mid]<nums[right]:
            return self.findMin(nums[ :mid+1])
        if nums[mid]>nums[left]:
            return self.findMin (nums[mid:])
