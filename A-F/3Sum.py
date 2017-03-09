# coding=utf-8
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length=len(nums)
        if length <=2:
            return []
        nums.sort()
        i=0
        res=[]
        while i<length-2:
            if i>0:
                if nums[i]==nums[i -1]:
                    i+=1
                    continue
            cur=0-nums[i]
            start=i+1
            end=length-1
            while start<end:
                if (end <length-1 and nums[end] ==nums[end+1]): 
                    end-=1
                    continue
                elif (start>i+1 and nums[start] ==nums[start-1]):
                    start+=1
                    continue
                sum=nums[start] +nums[end]
                if sum>cur:
                    end-=1
                elif sum<cur:
                    start+=1
                else:
                    res.append ([nums[i] ,nums[start] ,nums[end]])
                    start+=1
                    end-=1
                #print res
            i+=1
        return res

