# coding=utf-8
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[0]*len(nums)
        mul=1
        flag=0
        index=-1
        for i in xrange(len(nums)):
            if nums[i]==0:
                flag+=1
                index=i
                if flag==2:
                    break
            else:
                mul*=nums[i]
        if flag==2:
            return res
        if flag==1:
            res[index]=mul
            return res
        for i in xrange(len(nums)):
            res[i]=mul/nums[i]
        return res
