# coding=utf-8
class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if z == 0:
            return True
        if x == 0:
            return y == z
        if y == 0:
            return x == z
        if z > x + y or z < 1:
            return False
        
        gcd = 1
        for i in xrange(2,min(x,y)+1 ):
            if x % i == 0 and y % i == 0:
                gcd = i
        if gcd == 1:
            return True

