# coding=utf-8
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        queue=[n]
        res=0
        while queue!=[]:
            res+=1
            frontier=[]
            for x in queue:
                m=int(math.sqrt(x))
                m2=m**2
                if m2==x:
                    return res
                while m>=1:
                    frontier.append(x -m2)
                    m=m-1
                    m2=m**2
            queue=frontier
                    
                 
