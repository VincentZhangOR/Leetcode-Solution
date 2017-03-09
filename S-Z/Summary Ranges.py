# coding=utf-8
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        n=len(nums)
        if n==0:
            return []
        if n==1:
            return [str(nums[0])]
        left=nums[0]
        right=nums[0]
        ans=[]
        for i in xrange(1,n):
            if i==n-1:
                
                if nums[i]!=nums[i -1]+1:
                    if left!=right:
                        ans.append (str(left)+'->' +str(right))
                    else:
                        ans.append (str(left))

                    ans.append(str (nums[i]))
                else:
                    ans.append(str (left)+'->'+str (nums[i]))
            elif nums[i]!=nums[i-1] +1:
                right=nums[i-1]
                if left!=right:
                    ans.append(str (left)+'->'+str (right))
                else:
                    ans.append(str (left))
                left=nums[i]
                right=nums[i]
            else:
                right=nums[i]


