# coding=utf-8
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {}
        for i in xrange(len(nums)):
            d[nums[i]] = i
        res = []
        for x in findNums:
            index = d[x]
            flag = 0
            for i in xrange(index+1, len(nums)):
                if nums[i] > x:
                    res.append(nums[i] )
                    flag = 1
                    break
            if flag == 0:
                res.append(-1)
        return res
