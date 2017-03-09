# coding=utf-8
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = ''
        for x in nums:
            s += str(x)
        temp = s.split('0')
        ans = 0
        for x in temp:
            ans = max(ans, len(x))
        return ans
