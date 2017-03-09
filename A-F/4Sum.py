# coding=utf-8
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        length, res, dic = len(nums ), set(), {}
        if length<4:
            return []
        nums.sort()
        for p in range(length-1):
            for q in range(p+1 ,length):
                sum2=nums[p]+nums[q]
                if sum2 not in dic:
                    dic[sum2]=[(p,q )]
                else:
                    dic[sum2].append ((p,q))
        for i in range(length-3):
            for j in range(i+1 ,length-2):
                T=target-nums[i] -nums[j]
                if T in dic:
                    for k in dic[T]:
                        if k[0]>j:
                            res.add ((nums[i],nums[j] ,nums[k[0]] ,nums[k[1]]))
                            #print 
