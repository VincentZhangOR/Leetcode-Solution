# coding=utf-8
class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        d = collections.defaultdict (int)
        
        def help(pos, nums):
            if len(nums) == 0:
                return 1
            key = pos, tuple(nums)
            if key in d:
                return d[key]
            for i in xrange(len(nums )):
                if nums[i] % pos == 0 or pos % nums[i] == 0:
                    d[key] += help (pos + 1, nums[:i] + nums[i+1:])
            return d[key]
        

