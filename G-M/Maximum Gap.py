# coding=utf-8
class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return 0
        ma = max(nums)
        mi = min(nums)
        bRange = max(1, int((ma - mi - 1) / (n - 1) + 1))
        bLen = (ma - mi) / bRange + 1
        bs = [None] * bLen
        for x in nums:
            loc = (x - mi) / bRange
            b = bs[loc]
            if b == None:
                b = {'min': x, 'max': x}
            else:
                b['min'] = min (b['min'], x)
                b['max'] = max (b['max'], x)
            bs[loc] = b
        res = 0
        pre = bs[0]['max']
        for i in xrange(1, bLen):
            if bs[i] == None:
                continue
            res = max(res, bs[i]['min'] - pre)
            pre = bs[i]['max']
        return res
