# coding=utf-8
class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        d = {}
        
        def topdown(arr):
            m = len(arr)
            if m <= 1:
                return sum(arr)
            x = tuple(arr)
            if x in d:
                return d[x]
            d[x] = max(arr[0] - topdown(arr[1:]), arr[ -1] - topdown(arr[:m -1]))
            return d[x]
            
        return topdown(nums) >= 0
