# coding=utf-8
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        n = len(words)
        elements = [0] * n
        for i, s in enumerate(words):
            for c in s:
                elements[i] |= 1 << (ord(c) - 97)
 
        ans = 0
        for i in xrange(n):
            for j in xrange(i + 1, n):
                if not (elements[i] & elements[j]):
                    ans = max(ans, len (words[i]) * len (words[j]))
        return ans
