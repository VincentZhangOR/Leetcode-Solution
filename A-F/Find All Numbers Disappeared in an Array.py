# coding=utf-8
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for x in nums:
            nums[abs(x)-1] = -abs (nums[abs(x)-1]) 
        return [i + 1 for i, x in enumerate(nums) if x>0]
