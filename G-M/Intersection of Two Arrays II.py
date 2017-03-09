# coding=utf-8
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d={}
        res=[]
        for x in nums1:
            if x not in d:
                d[x]=1
            else:
                d[x]+=1
        for y in nums2:
            if y in d and d[y]>0:
                d[y]-=1
                res.append(y)
        return res
