# coding=utf-8
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        flag = 0
        if num < 0:
            flag = 1
            num = abs(num)
        #print num
        res = ''
        while num > 0:
            bit = num % 7
            res = str(bit) + res
            num /= 7
            #print res
        if flag == 1:
            res = '-' + res
        return res
