# coding=utf-8
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        d = collections.defaultdict (lambda: collections .defaultdict(int))
        #d[0] = {nums[0]:1, -nums[0] :1}
        n = len(nums)
        for i in xrange(n):
            if i == 0:
                d[i][nums[i]] += 1
                d[i][-nums[i]] += 1
            for x in d[i-1]:
                d[i][x+nums[i]] += d[i -1][x]
                d[i][x-nums[i]] += d[i -1][x]
                #print i, x, d
        return d[n-1][S]
