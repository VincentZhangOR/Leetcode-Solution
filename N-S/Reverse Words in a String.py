# coding=utf-8
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = s.split(' ')
        l.reverse()
        res = ''
        for x in l:
            if x == '':
                continue
            res += x + ' '
        return res[:-1]
