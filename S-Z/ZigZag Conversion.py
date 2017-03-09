# coding=utf-8
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows<=1 or len(s )<=numRows:
            return s
        l=['']*numRows
        index,step=0,1
        for x in s:
            l[index] += x
            if index==0:
                step=1
            elif index==numRows-1:
                step=-1
            index+=step
            
        return ''.join(l)
            
