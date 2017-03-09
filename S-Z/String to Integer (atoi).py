# coding=utf-8
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        d={'1','2','3','4','5','6','7' ,'8','9','0'}
        
        str=str.lstrip()
        if len(str) is 0:
            return 0

        
        flag=0
        i=0
        
        if str[i]=='-':
            flag=1
            i+=1
        elif str[0]=='+':
            i+=1
            
        ans=0

        while len(str)>i and str[i] in d:
            ans = 10*ans + int(str[i])
            i+=1
            
        if flag==1:
            ans = 0-ans
        if ans > 2147483647:
            return 2147483647
        if ans < -2147483648:
            return -2147483648
        return ans
