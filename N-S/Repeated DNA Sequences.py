# coding=utf-8
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        d={}
        ans=[]
        for i in xrange(len(s)-9):
            if s[i:i+10] in d:
                if d[s[i:i+10]]==1:
                    ans.append(s[i:i +10])
                    d[s[i:i+10]]=2
            else:
                d[s[i:i+10]]=1

        return ans
                
