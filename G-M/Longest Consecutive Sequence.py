# coding=utf-8
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={x:False for x in nums}
        ans=0
        for i in d:
            if d[i]==False:
                d[i]=True
                longth=1
                cur=i+1
                while cur in d and d[cur] is False:
                    d[cur]=True
                    longth+=1
                    cur+=1
                cur=i-1
                while cur in d and d[cur] is False:
                    d[cur]=True
                    longth+=1
                    cur-=1
                ans=max(ans,longth)
        return ans

