# coding=utf-8
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length=len(nums)
        res=0
        if length<=3:
            for x in nums:
                res+=x
            return res
        nums.sort()
        ans=abs(nums[0]+nums[1] +nums[2]-target)
        i=0
        #print nums
        while i<length-2:
            if i>0 and nums[i-1] ==nums:
                continue
            start=i+1
            end=length-1
            cur=nums[i]-target
            while start<end:
                if start>i+1 and nums[start-1] ==nums[start]:
                    start+=1
                    continue
                elif end<length-1 and nums[end+1] ==nums[end]:
                    end-=1
                    continue
                else:
                    sum=nums[i] +nums[start] +nums[end]
                    if sum-target<0:
                        start+=1
                    elif sum-target >0:
                        end-=1
                    else:
                        return target
                    if (abs(sum -target)<=ans):
                        ans=abs(sum -target)
                        res=sum
              
                #print nums[i] ,nums[start] ,nums[end],sum,ans
