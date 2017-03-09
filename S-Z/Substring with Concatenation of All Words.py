# coding=utf-8
class Solution(object):
    def findSubstring(self, s, words ):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        d = collections.defaultdict (int)
        for x in words:
            d[x] += 1
        res = []
        n = len(words[0]) if len (words) > 0 else 0
        m = len(words)
        ls = len(s)
        cur = collections .defaultdict(int)
        flag = 0
        for i in xrange(ls - n*m + 1 ):
            flag = 0
            for j in xrange(i,i+n*m ,n):
                temp = s[j:j+n]
                
                cur[temp] += 1
                #print temp,cur
                if cur[temp] > d[temp]:
                    flag = 1
                    break
            if flag == 0 and j == i +n*(m-1):
                res.append(i)

