# coding=utf-8
class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        stack = [1]
        res = []
        while stack != []:
            temp = stack.pop()
            res.append(temp)
            if temp < n and temp % 10 < 9:
                stack.append(temp + 1)
            if temp * 10 <= n:
                stack.append(temp * 10 )
        return res
