# coding=utf-8
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d1=set()
        d2=set()
        for x in nums1:
            d1.add(x)
        for y in nums2:
            d2.add(y)
        return list(d1.intersection(d2 ))
