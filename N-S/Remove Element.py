# coding=utf-8
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length=len(nums)
        if length==0:
            return 0
        if val not in nums:
            return length
        nums.sort()
        i=0
        while i<len(nums):
            if nums[i]<val:
                i+=1
                continue
            elif nums[i]==val:
                del nums[i]
            else:
                break

        res=len(nums)
        return res

