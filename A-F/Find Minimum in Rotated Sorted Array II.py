# coding=utf-8
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        right=len(nums)-1
        while left < right and nums[left] >= nums[right]:
            mid = (left + right) / 2
            if nums[mid] > nums[left]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                left += 1
        return nums[left]
        
        
