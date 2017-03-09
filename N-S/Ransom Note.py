# coding=utf-8
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        d1={}
        d2={}
        for x in magazine:
            if x not in d1:
                d1[x]=1
            else:
                d1[x]+=1
        for x in ransomNote:
            if x not in d1:
                return False
            else:
                if d1[x]==0:
                    return False
                else:
                    d1[x]-=1
        return True
