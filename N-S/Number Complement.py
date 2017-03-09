# coding=utf-8
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        temp = bin(num)[2:]
        ans = ''
        for x in temp:
            if x == '0':
                ans += '1'
            else:
                ans += '0'
        return int(ans,2)
