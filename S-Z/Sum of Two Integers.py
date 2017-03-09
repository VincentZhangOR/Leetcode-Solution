# coding=utf-8
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MAX_INT = 0x7FFFFFFF
        MIN_INT = 0x80000000
        MASK = 0x100000000
        if b==0:
            if a <= MAX_INT:
                return a
            else:
                return ~((a % MIN_INT) ^ MAX_INT)
        sum = (a ^ b) % MASK
        carry = ((a & b)<<1) % MASK
        return self.getSum(sum,carry)
