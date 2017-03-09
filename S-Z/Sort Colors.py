# coding=utf-8
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in -place instead.
        """
        left=0
        right=len(nums)-1
        count=0
        zero=0
        for x in nums:
            if x==0:
                zero+=1
            else:
                #zero+=1
                break
        left=zero
        while left<right:
            #print nums,zero,count
            if nums[left]==0:
                if count>0:
                    nums[zero]=0
                    zero+=1
                    count-=1
                    nums[left]=1
                else:
                    left+=1
                    zero+=1
                continue
            if nums[right]==2:
                right-=1
                continue
            if nums[left]==2:
                temp=nums[left]
                nums[left]=nums[right]
                nums[right]=temp
                right-=1
                continue
            if nums[right]==0:
                if count>0:
                    nums[zero]=0
                    zero+=1
                    count-=1
                    nums[right]=1
                else:
                    temp=nums[left]
                    nums[left] =nums[right]
                    nums[right]=temp
                    left+=1
                    zero+=1
                continue
            if nums[left]==1:
                count+=1
                left+=1
                continue
                
