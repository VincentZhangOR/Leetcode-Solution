# coding=utf-8
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        n = len(intervals)
        new = []
        d = collections.defaultdict (lambda: float("inf"))
        for i in xrange(n):
            new.append(intervals[i] .start)
            d[intervals[i].start] = min(i,d[intervals[i] .start])
        new.sort()
        res = []
        for i in xrange(n):
            temp = bisect .bisect_left(new, intervals[i].end)
            if temp >= n:
                res.append(-1)
            else:
                res.append (d[new[temp]])

