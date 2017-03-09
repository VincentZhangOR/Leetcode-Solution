# coding=utf-8
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = collections.defaultdict (int)
        nums = [1] + nums + [1]
        
        n = len(nums)
        
        def topdown(i,j):
            if (i,j) in d:
                return d[i,j]
            #if i == j:
            #    d[i,j] = 1
            #    return d[i,j]
            #if i + 1 == j:
            #    d[i,j] = 0
            #    return d[i,j]
            for k in xrange(i+1,j):
                d[i,j] = max(d[i,j], nums[i]*nums[k] *nums[j] + topdown (i,k) + topdown(k ,j))
            #print i,j,d[i,j]
            return d[i,j]
        

