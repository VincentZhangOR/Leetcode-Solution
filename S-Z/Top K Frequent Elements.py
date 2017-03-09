# coding=utf-8
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d={}
        for x in nums:
            if x not in d:
                d[x]=1
            else:
                d[x]+=1
        mid=sorted(d.iteritems(), key =lambda d:d[1], reverse = True)
        res=[]
        for i in xrange(k):
            res.append(mid[i][0])
        return res
