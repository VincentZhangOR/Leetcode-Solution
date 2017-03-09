# coding=utf-8
class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        ans = 1
        for x in b[::-1]:
            ans = ans * a ** x % 1337
            a = a ** 10 % 1337
        return ans
