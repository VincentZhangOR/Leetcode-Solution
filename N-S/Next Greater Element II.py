# coding=utf-8
class Solution(object):
    def nextGreaterElements(self, nums ):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        stack = []
        res = []
        n = len(nums)
        d = [-1] * n
        for i in xrange(n*2):
            x = i % n
            while stack and nums[stack[-1]] < nums[x]:
                d[stack.pop()] = nums[x]
            stack.append(x)
        return d
        
                
