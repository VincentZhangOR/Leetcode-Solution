# coding=utf-8
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        n, m = len(s), len(p)
        
        d = collections.defaultdict (lambda: False)
        d[-1,-1] = True
        for i in xrange(m):
            if p[i] == '*':
                if i >= 1:
                    d[-1,i] = d[-1,i -2]
                    
        def topdown(i,j):
            #print i,j,d
            if (i,j) in d:
                return d[i,j]
            if j < 0 or i < 0:
                d[i,j] = False
                return d[i,j]
            if p[j] == '.':
                d[i,j] = topdown(i-1 ,j-1)
            elif p[j] == '*':
                d[i,j] = topdown(i,j -1) or topdown(i,j -2) or (topdown(i -1,j) and (s[i] == p[j-1] or p[j-1] == '.'))
            else:
                d[i,j] = topdown(i-1 ,j-1) and s[i] == p[j]
            return d[i,j]
        
        return topdown(n-1,m-1)
        
        '''
        for i in xrange(n):
            for j in xrange(m):
                #print i,j,d
                if p[j] == '.':
                    d[i,j] = d[i-1,j -1]
                elif p[j] == '*':
                    d[i,j] = d[i,j -1] or d[i,j-2] or (d[i-1,j] and (s[i] == p[j-1] or p[j-1] == '.'))
                else:

