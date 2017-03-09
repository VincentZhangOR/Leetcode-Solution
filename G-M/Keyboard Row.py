# coding=utf-8
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        s1 = {'Q','q','W','w','E','e' ,'R','r','T','t','Y','y' ,'U','u','I','i','O','o' ,'P','p'}
        s2 = {'A', 'S','D','F','G','H' ,'J','K','L','a','s','d' ,'f','g','h','j','k','l'}
        s3 = {'Z','X','C','V','B','N' ,'M','z','x','c','v','b' ,'n','m'}
        res = []
        for x in words:
            if len(x) == 1:
                res.append(x)
                continue
            flag = 0
            for i in xrange(len(x)):
                if i == 0:
                    if x[i] in s1:
                        flag = 1
                    elif x[i] in s2:
                        flag = 2
                    else:
                        flag = 3
                else:
                    if flag == 1 and x[i] not in s1:
                        break
                    elif flag == 2 and x[i] not in s2:
                        break
                    elif flag == 3 and x[i] not in s3:
                        break
                if i == len(x) - 1:
                    res.append(x)
        return res
