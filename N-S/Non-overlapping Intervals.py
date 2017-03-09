# coding=utf-8
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        lo = sorted(intervals, key = lambda x: x.end)
        fo = sorted(intervals, key = lambda x: x.start)
        d = set()
        res = 0
        point = 0
        n = len(intervals)
        for x in lo:
            flag = 0
            if x in d:
                continue
            s = x.start
            e = x.end
            while point < n:
                if fo[point].start >= e:
                    break
                if fo[point] == x and flag == 0:
                    point += 1
                    flag = 1
                    continue
                d.add(fo[point])
                point += 1
                res += 1

