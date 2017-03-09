# coding=utf-8
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        canReach=0
        leng=len(nums)
        for i in xrange(leng):
            if i <= canReach:
                canReach=max(canReach, i+nums[i])
            if canReach >= leng-1:
                return True
        return False
