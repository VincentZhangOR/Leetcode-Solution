# coding=utf-8
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        res = 0
        i = 0
        while i < n-1:
            dis = 0
            next = 0
            for j in xrange(1,nums[i] +1):
                if i+j >= n-1:
                    return res+1
                temp = nums[i+j] + j
                if temp > dis:
                    next = j
                    dis = temp
            #print "1111111", i, next ,res
            i += next
            res += 1
            #print i,res

            
        return res
