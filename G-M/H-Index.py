# coding=utf-8
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        d=[]
        N=len(citations)
        for i in xrange(len(citations )):
            if citations[i]>=i+1:
                d.append(i+1)
        if d==[]:
            return 0
        else:
            return sorted(d,reverse =True)[0]
