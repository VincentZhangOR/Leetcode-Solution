# coding=utf-8
class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        d = collections.defaultdict (lambda: False)
        n = len(s1)
        if (s1,s2) in d:
            return d[s1,s2]
        if s1 == s2:
            d[s1,s2] = True
            return d[s1,s2]
        if sorted(s1) != sorted(s2) or len(s1) != len(s2):
            d[s1,s2] = False
            return d[s1,s2]
        for k in xrange(1,n):
            if (self.isScramble(s1[:k] ,s2[:k]) and self .isScramble(s1[k:] ,s2[k:])) or (self .isScramble(s1[:k],s2[ -k:]) and self .isScramble(s1[k:],s2[ :-k])):
                d[s1,s2] = True
                return d[s1,s2]
        return d[s1,s2]
