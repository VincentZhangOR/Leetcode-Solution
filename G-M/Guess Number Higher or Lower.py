# coding=utf-8
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left=1
        right=n
        while True:
            mid=(left+right)/2
            res=guess(mid)
            if res==-1:
                right=mid-1
            elif res==1:
                left=mid+1
            else:
                return mid
