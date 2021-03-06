# coding=utf-8
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1=len(nums1)
        len2=len(nums2)
        length=len1+len2
        if length%2==1:
            return self.getKth(nums1 ,nums2,length/2+1)
        else:
            return (self.getKth(nums1 ,nums2,length/2)+self .getKth(nums1,nums2 ,length/2+1))/2.0
            
    def getKth(self, A, B, k):
        lenA=len(A)
        lenB=len(B)
        if lenA>lenB:
            return self.getKth(B,A,k)
        if lenA==0:
            return B[k-1]
        if k==1:
            return min(A[0],B[0])
        pa=min(k/2,lenA)
        pb=k-pa
        if A[pa-1]<=B[pb-1]:
            return self.getKth(A[pa:] ,B,pb)
        else:
            return self.getKth(A,B[pb :],pa)
        
        
        
