# coding=utf-8
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key = lambda x: x.start)
        res = []
        if len(intervals) == 0:
            return res
        start = end = None
        for i in xrange(len (intervals)):
            if start == None:
                start = intervals[i] .start
            temp = end
            end = max(temp ,intervals[i].end)
            if i<len(intervals) - 1:
                if end >= intervals[i+1] .start:
                    continue
                else:
                    res.append (Interval(start, end))
                    start = None
            else:
                if res == [] or res[ -1].end != intervals[-1].end:
                    res.append
