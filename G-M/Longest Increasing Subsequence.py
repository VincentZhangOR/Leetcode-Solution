# coding=utf-8
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums==[] or nums==None:
            return 0
        n=len(nums)
        d=[1]*n
        ans=1
        for i in xrange(1,n):
            for j in xrange(i):
                if nums[j]<nums[i]:
                    d[i]=max(d[j]+1 ,d[i])
            ans=max(ans,d[i])
        return ans
