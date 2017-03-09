# coding=utf-8
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        a=reduce(operator.xor, nums)
        b=reduce(operator.xor, xrange (len(nums)+1))
        return a^b
        '''
        
        temp = 0
        for x in nums:
            temp += x
        return sum(xrange(len(nums)+1 )) - temp
