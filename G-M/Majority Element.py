# coding=utf-8
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)
        #if l==1:
        #    return nums[0]
        nums.sort()
        #left=nums[:l/2]
        #right=nums[l/2:]
        #if left[-1]!=right[0]:
        #    return right[0]
        #else:
        return nums[l/2]
        
            
