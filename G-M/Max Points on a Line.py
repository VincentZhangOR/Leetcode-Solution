# coding=utf-8
# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

import numpy as np

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        n = len(points)
        #decimal.getcontext().prec = 13
        if n <= 2:
            return n
        res = 2
        for i in xrange(n-1):
            sameP = 0
            d = collections .defaultdict(lambda: 1.0)
            for j in xrange(i+1, n):
                if points[i].x == points[j].x and points[i].y == points[j].y:
                    sameP += 1
                elif points[i].x == points[j].x:
                    d['inf'] += 1
                else:
                    k = np .longdouble (points[i].y - points[j].y) / (points[i].x - points[j].x)
                    #print i,j,k,d
                    d[k] += 1
            #print i,j,d
            temp = 1 if len(d) == 0 else max(d.values())

