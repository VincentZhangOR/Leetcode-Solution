# coding=utf-8
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 <= 0 or n2 <= 0:
            return []
        res = []
        used = set()
        h = [(nums1[0] + nums2[0], 0, 0)]
        while len(h) > 0:
            if len(res) == k:
                break
            sum, a, b = heapq.heappop (h)
            res.append([nums1[a] ,nums2[b]])
            if a+1 < n1 and (a+1,b) not in used:
                heapq.heappush(h ,(nums1[a+1] +nums2[b],a+1,b))
                used.add((a+1,b))
            if b+1 < n2 and (a,b+1) not in used:
                heapq.heappush(h ,(nums1[a]+nums2[b +1],a,b+1))
                used.add((a,b+1))
            #print res
        return res
