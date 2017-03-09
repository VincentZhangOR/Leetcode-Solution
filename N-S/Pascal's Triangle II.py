# coding=utf-8
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex==0:
            return [1]
        if rowIndex==1:
            return [1,1]
        if rowIndex==2:
            return [1,2,1]
        res=[1,2,1]+[0]*(rowIndex-2)
        for i in xrange(rowIndex-2):
            j=1
            temp2=res[0]
            while j<=len(res)-1 and res[j]>0:
                temp1=res[j]
                res[j]=temp2+res[j]
                temp2=temp1
                j+=1
                #print res
            res[j]=1
        return res
