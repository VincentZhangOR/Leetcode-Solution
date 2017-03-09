# coding=utf-8
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        left=0
        right=0
        sum=0
        size=len(nums)
        ans=size+1
        while right<size:
            while right<size and sum<s :
                sum+=nums[right]
                right+=1
            while left<right and sum >=s:
                ans=min(ans,right-left )
                sum-=nums[left]
                left+=1
        return [0, ans][ans<=size]
