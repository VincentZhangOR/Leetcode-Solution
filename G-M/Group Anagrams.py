# coding=utf-8
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        cur={}
        res=[]
        for x in strs:
            sortedx=''.join(sorted(x))
            if sortedx not in cur:
                cur[sortedx]=[x]
            else:
                cur[sortedx]+=[x]
        #print cur
        for x in cur:
            res.append(cur[x])
        return res
