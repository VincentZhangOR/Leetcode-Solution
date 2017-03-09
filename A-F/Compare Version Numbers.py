# coding=utf-8
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        #if version1==version2:
        #    return 0
        a=version1.split('.')
        b=version2.split('.')
        l=min(len(a),len(b))
        for i in xrange(l):
            a[i]=int(a[i])
            b[i]=int(b[i])
            if a[i]>b[i]:
                return 1
            elif a[i]<b[i]:
                return -1
            else:
                continue
        if len(a)==l:
            for j in xrange(l,len(b)):
                b[j]=int(b[j])
                if b[j]!=0:
                    return -1
            return 0
        if len(b)==l:
            for j in xrange(l,len(a)):
                a[j]=int(a[j])
                if a[j]!=0:
                    return 1
            return 0
