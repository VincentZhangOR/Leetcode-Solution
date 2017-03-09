# coding=utf-8
class Solution(object):
    def wordBreak(self, s, wordDict ):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        word = set()
        d = {}
        for x in wordDict:
            word.add(x)
            
        
        
        def topdown(i,j):

            if (i,j) in d:
                return d[i,j]
            if i > j:
                d[i,j] = []
                return d[i,j]
            if i == j:
                d[i,j] = [[s[i]]] if s[i] in word else []
                return d[i,j]
            d[i,j] = []
            for k in xrange(i,j+1):
                now = s[i:k+1]

                if now not in word:
                    continue
                temp = topdown(k+1,j )
                
                if temp == [] and k == j:
                    d[i,j].append ([now])
                    continue
                for x in temp:
                    d[i,j].append (([now] + x))
                
            return d[i,j]
        
        ans = topdown(0,len(s)-1)
        res = []
        for x in ans:
            res.append(' '.join(x))

