# coding=utf-8
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) >> 1
            if n - mid > citations[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return n - left
