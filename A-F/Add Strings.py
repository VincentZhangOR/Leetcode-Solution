# coding=utf-8
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        a = num1[::-1]
        b = num2[::-1]
        la, lb = len(a), len(b)
        carrier = 0
        res = ""
        for x,(i,j) in enumerate(zip(a ,b)):
            i, j = int(i), int(j)
            cur = i+j+carrier
            temp = cur % 10
            carrier = cur / 10
            res = str(temp) + res
        x += 1
        while x < la:
            cur = int(a[x]) + carrier
            temp = cur % 10
            carrier = cur / 10
            res = str(temp) + res
            x += 1
        while x < lb:
            cur = int(b[x]) + carrier
            temp = cur % 10
            carrier = cur / 10
            res = str(temp) + res
            x += 1
        if carrier == 1:
            res = str(carrier) + res
        return res
