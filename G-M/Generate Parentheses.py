# coding=utf-8
import random
class Solution(object):
    def generateParenthesis(self, n ):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        res = []
        self.helpler(n, n, '', res)
        return res
        
    def helpler(self, l, r, item, res):
        if r < l:
            return
        if l == 0 and r == 0:
            res.append(item)
        if l > 0:
            self.helpler(l - 1, r, item + '(', res)
        if r > 0:
            self.helpler(l, r - 1, item + ')', res)


