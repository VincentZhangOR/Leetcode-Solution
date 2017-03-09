# coding=utf-8
class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        n = len(S) - S.count('-')
        f = n % K
        c = 0
        tc = 0
        g = 1 if f != 0 else 2
        res = ''
        for x in S:
            if x == '-':
                continue
            
            res += x.upper()
            c += 1
            tc += 1
            #print c, tc
            if c == f and g == 1:
                g += 1
                c = 0
                if tc < n:
                    res += '-'
            elif c == K and g > 1:
                c = 0
                if tc < n:
                    res += '-'
            #print c,f,K,res
        return res
