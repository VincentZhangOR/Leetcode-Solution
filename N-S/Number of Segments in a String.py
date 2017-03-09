# coding=utf-8
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = s.split(' ')
        ans = 0
        for x in a:
            if x != '':
                ans+=1
        return ans
