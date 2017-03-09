# coding=utf-8
class Solution(object):
    def constructRectangle(self, area ):
        """
        :type area: int
        :rtype: List[int]
        """
        mid = int(math.ceil(math.sqrt (area)))
        for i in xrange(mid, area):
            if area % i == 0:
                return [i, area/i]
        return [area, 1]
