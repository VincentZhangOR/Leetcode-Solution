# coding=utf-8
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length=len(s)
        if length<2:
            return s
        res=''
        i=0
        while i<length:
            cur=self.helper(s,i,i)
            if len(cur)>len(res):
                res=cur
            cur=self.helper(s,i,i+1)
            if len(cur)>len(res):
                res=cur
            i+=1
        return res
            
    def helper(self,s,a,b):
        length=len(s)
        while a>=0 and b<length and s[a]==s[b]:
            a-=1
            b+=1
        #print 'a:',a,'b:',b
        return s[a+1:b]
        
