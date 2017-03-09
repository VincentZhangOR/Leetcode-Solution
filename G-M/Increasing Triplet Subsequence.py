# coding=utf-8
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a=b=None
        for x in nums:
            if a==None or a>=x:
                a=x
            elif b==None or b>=x:
                b=x
            else:
                return True
        return False
