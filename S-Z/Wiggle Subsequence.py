# coding=utf-8
class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        diff = []
        
        for i in xrange(len(nums)-1 ):
            diff.append(nums[i+1] -nums[i])
        if diff == [0] * (len(nums )-1):
            return 1
        #print diff
        #res1, res2 = 0, 0
        res = 1
        j = 0
        #temp = diff[0]
        for i in xrange(1,len(diff )):
            if diff[j] == 0:
                j += 1
                continue
            if diff[i] * diff[j] < 0
