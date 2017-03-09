# coding=utf-8
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        heaters.sort()
        n = len(heaters)
        ans = 0
        for x in houses:
            leftr, rightr = float ('inf'), float('inf' )
            index = bisect .bisect_right (heaters,x)
            if index > 0:
                leftr = x - heaters[index-1]
            index = bisect .bisect_left(heaters ,x)
            if index < n:
                rightr = heaters[index] - x
            
            r = min(leftr, rightr)
            if r > ans:
                ans = r

