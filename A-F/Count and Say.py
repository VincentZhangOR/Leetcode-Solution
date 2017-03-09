# coding=utf-8
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==1:
            return '1'
        if n==2:
            return '11'
        res='11'
        i=2
        
        while i < n:
            count=1
            mid=res
            res=''
            for j in xrange(len(mid)-1 ):
                if j==len(mid)-2:
                    if mid[j]==mid[j +1]:
                        count+=1
                        res+=str(count )+str(mid[j])
                    else:
                        res+=str(count )+str(mid[j])+str(1 )+str(mid[j+1])
                else:
                    if mid[j]==mid[j +1]:
                        count+=1
                    else:
                        res+=str(count )+str(mid[j])
                        count=1
                
            i+=1
        return res
        
