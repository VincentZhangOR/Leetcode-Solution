# coding=utf-8
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums==[]:
            return False
        d=set()
        for x in nums:
            if x in d:
                return True
            else:
                d.add(x)
        return False
