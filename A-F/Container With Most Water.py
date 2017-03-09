# coding=utf-8
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        if length < 2:
            return 0
        i=0
        j=length-1
        res=0
        cur=0
        while i<j:
            cur=min(height[i] ,height[j])*(j-i)
            res=max(res,cur)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return res
