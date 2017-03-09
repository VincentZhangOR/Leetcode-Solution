# coding=utf-8
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        n = len(p)
        m = len(s)
        counts = collections.Counter(p )
        new = collections.Counter()
        for i in xrange(m):
            new[s[i]] += 1
            if i>=n:
                new[s[i-n]] -= 1
                if new[s[i-n]]==0:
                    del new[s[i-n]]
            if new == counts:
                res.append(i-n+1)
        return res
