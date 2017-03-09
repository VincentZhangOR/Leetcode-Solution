# coding=utf-8
class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        d = collections.defaultdict (int)
        n = len(picture)
        m = len(picture[0])
        for i in xrange(n):
            count = 0
            temp = []
            for j in xrange(m):
                if picture[i][j] == 'B':
                    count += 1
                    d[j] += 1
                    temp.append(j)
            if count > 1:
                for x in temp:
                    d[x] += 1
        res = 0
        for x in d:
            if d[x] == 1:

