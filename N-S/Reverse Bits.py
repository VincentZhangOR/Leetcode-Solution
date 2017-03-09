# coding=utf-8
class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        mid=bin(n)
        mid=mid[2:]
        mid=mid[::-1]
        while len(mid)<32:
            mid+='0'
        #print mid[:32]
        return int(mid,2)
