# coding=utf-8
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        lo=matrix[0][0]
        hi=matrix[-1][-1]
        
        while lo<=hi:
            mid=(lo+hi)/2
            loc=0
            for x in matrix:
                loc+=bisect .bisect_right(x,mid )
            if loc>=k:
                hi=mid-1
            else:
                lo=mid+1
            print lo,hi,mid,loc
        return lo
