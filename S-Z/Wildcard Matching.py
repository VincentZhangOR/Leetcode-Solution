# coding=utf-8
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        n, m = len(s), len(p)
        flagP = -1
        flagS = 0
        ps, pp = 0, 0
        while ps < n:
            if pp < m and (p[pp] == ' ?' or s[ps] == p[pp]):
                ps += 1
                pp += 1
            elif pp < m and p[pp] == ' *':
                flagP = pp
                pp += 1
                flagS = ps
            elif flagP != -1:
                pp = flagP + 1
                flagS += 1
                ps = flagS
            else:
                return False
        while pp < m:
            if p[pp] != '*':
                return False
            pp += 1
        return True
