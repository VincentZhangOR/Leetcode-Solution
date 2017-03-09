# coding=utf-8
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in -place instead.
        """
        if 0 not in nums:
            return
        length = len(nums)
        i=0
        j=length-1
        while i<j:
            if nums[j]==0:
                j-=1
                continue
            if nums[i]==0:
                del nums[i]
                nums.append(0)
                j-=1
            else:
                i+=1
        return
                
