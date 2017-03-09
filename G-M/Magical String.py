# coding=utf-8
class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = '122'
        p = 2
        while len(res) < n:
            res += str(3 - int(res[-1] )) * int(res[p])
            p += 1
        return res[:n].count('1')
