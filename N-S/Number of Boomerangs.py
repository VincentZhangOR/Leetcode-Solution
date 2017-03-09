# coding=utf-8
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        res = 0
        n = len(points)
        for i in xrange(n):
            d = {}
            x0,y0 = points[i][0] ,points[i][1]
            for j in xrange(n):
                x1,y1 = points[j][0] ,points[j][1]
                dis=(x0-x1)*(x0-x1 )+(y0-y1)*(y0-y1)
                d[dis] = d.get(dis,0 )+1
            for x in d:
                res += d[x]*(d[x]-1)
        return res
                
