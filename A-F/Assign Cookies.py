# coding=utf-8
class Solution(object):
    def findContentChildren(self, g, s ):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort(reverse=True)
        s.sort(reverse=True)
        ans = 0
        j = 0
        for i in xrange(len(g)):
            if j >= len(s):
                break
            if g[i] <= s[j]:
                ans += 1
                j += 1
        return ans
