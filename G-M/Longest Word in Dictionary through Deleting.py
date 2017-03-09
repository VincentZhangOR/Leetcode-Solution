# coding=utf-8
class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        d.sort()
        n = len(s)
        words = len(d)
        res = ''
        for i in xrange(words):
            m = len(d[i])
            p, q = 0, 0
            cnt = 0
            while p < m and q < n:
                if d[i][p] == s[q]:
                    p += 1
                    q += 1
                    cnt += 1
                else:
                    q += 1
            if p == m and len(res) < cnt:
                res = d[i]
        return res
                
