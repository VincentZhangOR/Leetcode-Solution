# coding=utf-8
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n==0:
            return 0
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0], nums[1])
        d=[0]*(n-1)
        return max(self.help(nums, d ), self.help(nums[1:n] +[nums[0]], d))
        
    def help(self, nums, d):
        d[0]=nums[0]
        d[1]=max(nums[0], nums[1])
        for i in xrange(2,len(nums )-1):
            d[i]=max(d[i-2]+nums[i] ,d[i-1])

