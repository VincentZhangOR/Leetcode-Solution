# coding=utf-8
class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        res = 0
        n = len(timeSeries)
        if n <= 0:
            return res
        for i in xrange(n-1):
            res += min(timeSeries[i+1] - timeSeries[i], duration)
        res += duration
        return res
                
