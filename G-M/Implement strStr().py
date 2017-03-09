# coding=utf-8
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        #res=-1
        if needle not in haystack:
            return -1
        m=len(haystack)
        n=len(needle)
        if n==0:
            return 0
        i=0
        j=0
        start=m
        cur=0
        while i<m:
            if haystack[i] ==needle[j]:
                start=min(start,i)
                #print start,i,j
                cur=start
                i+=1
                j+=1
                
            else:
                j=0
                i=cur+1
                if haystack[i]! =needle[j]:
                    i+=1
                    cur+=1
                start=m
            #print i,haystack[i],j ,needle[j]
            if j==n:
                return start

