# coding=utf-8
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        if n <= 2:
            return 0
        d = collections.defaultdict (lambda:(0,0,0))
        d[1] = (0,A[1]-A[0],2)
        for i in xrange(2,n):
            ans, ldiff, ln = d[i-1]
            if A[i] - A[i-1] == ldiff:
                #if ln >= 2:
                d[i] = (ans + ln - 1, ldiff, ln + 1)
                #else:
                #    d[i] = (ans, ldiff, ln + 1)
            else:
                d[i] = (ans, A[i] - A[i-1], 2)
        return d[n-1][0]
