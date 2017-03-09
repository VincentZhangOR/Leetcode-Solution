# coding=utf-8
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)/2
            if nums[mid]==target:
                if nums[left]! =target:
                    for i in xrange (mid,left-1,-1): 
                        if nums[i]! =target:
                            left=i+1
                            break
                if nums[right]! =target:
                    for j in xrange (mid,right+1):
                        if nums[j]! =target:
                            right=j -1
                            break
                return [left,right]
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return [-1,-1]

