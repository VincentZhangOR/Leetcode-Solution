# coding=utf-8
class Solution(object):
    def fourSumCount(self, A, B, C, D ):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        d = collections.defaultdict (int)
        n = len(A)
        ans = 0
        for i in xrange(n):
            for j in xrange(n):
                d[A[i]+B[j]] += 1
        for i in xrange(n):
            for j in xrange(n):
                if -(C[i]+D[j]) in d:
                    ans += d[-(C[i] +D[j])]
        return ans
