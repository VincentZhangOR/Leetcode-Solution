# coding=utf-8
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        left = 1
        right = n
        mid = (left+right)/2
        while n<(1+mid)*mid/2 or n>=(1 +mid)*(2+mid)/2:
            if n<(1+mid)*mid/2:
                right = mid
            elif n>=(1+mid)*(2+mid)/2:
                left = mid
            mid = (left+right)/2
        return mid
