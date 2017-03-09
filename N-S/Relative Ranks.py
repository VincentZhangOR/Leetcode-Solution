# coding=utf-8
class Solution(object):
    def findRelativeRanks(self, nums ):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        
        n = len(nums)
        h = zip(map(lambda x: -x, nums),range(n))
        heapq.heapify(h)
        #print h
        count = 1
        res = [0 for x in xrange(n)]
        while h:
            a, b = heapq.heappop(h)
            #print a,b
            if count == 1:
                res[b] = 'Gold Medal'
            elif count == 2:
                res[b] = 'Silver Medal'
            elif count == 3:
                res[b] = 'Bronze Medal'

