# coding=utf-8
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n1=None
        n2=None
        c1=0
        c2=0
        for x in nums:
            if x==n1:
                c1+=1
            elif x==n2:
                c2+=1
            elif c1==0:
                n1=x
                c1=1
            elif c2==0:
                n2=x
                c2=1
            else:
                c1-=1
                c2-=1
        n=len(nums)
        res=[]
        print n1,n2
        for x in (n1,n2):
            if nums.count(x)>n/3 and x!=None:
                res.append(x)
        return res
