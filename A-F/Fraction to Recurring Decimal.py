# coding=utf-8
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        flag = numerator * denominator < 0
        n = abs(numerator)
        m = abs(denominator)
        d = {}
        temp = []
        count = 0
        repeat = None
        while True:
            temp.append(str(n / m))
            count += 1
            n = 10 * (n % m)
            if n == 0:
                break
            if n in d:
                repeat = (d[n], count)
                break
            d[n] = count
        res = temp[0]
        if len(temp) > 1:
            res += '.'
        if repeat != None:
            res += ''.join(temp[1 :repeat[0]]) + '(' + ''.join(temp[repeat[0] :count]) + ')'
        else:
            res += ''.join(temp[1:])
        if flag == True:
            res = '-' + res
        return res
