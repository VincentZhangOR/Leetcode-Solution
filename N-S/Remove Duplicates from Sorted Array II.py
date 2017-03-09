# coding=utf-8
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums==[]:
            return 0
        i=0
        j=1
        flag=0
        while j<len(nums):
            if nums[i]==nums[j]:
                if flag==0:
                    flag=1
                    i+=1
                    nums[i]=nums[j]
            else:
                i+=1
                nums[i]=nums[j]
                flag=0
            j+=1
            #print nums,i,j
        return i+1
