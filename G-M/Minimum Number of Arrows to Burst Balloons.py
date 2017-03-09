# coding=utf-8
class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        lo = sorted(points, key = lambda (x, y) : y)
        #print lo
        fo = sorted(points)
        d = set()
        ans = 0
        point = 0
        n = len(points)
        for x in lo:
            s, e = x
            if (s,e) in d:
                continue
            ans += 1
            while point < n:
                if fo[point][0] <= e :
                    d.add ((fo[point][0] ,fo[point][1]))
                    point += 1

