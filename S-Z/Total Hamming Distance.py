# coding=utf-8
class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        res = 0
        ma = len(bin(max(nums))) - 2
        while ma > 0:
            #temp = map(lambda x: x % 2, nums)
            count = len(filter(lambda x: x % 2 == 1, nums))
            res += count * (n-count)
            nums = map(lambda x: x / 2 , nums)
            #print temp, count, nums
            ma -= 1
        return res
