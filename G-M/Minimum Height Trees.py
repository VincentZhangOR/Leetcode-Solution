# coding=utf-8
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]
        if n == 2:
            return [0,1]
        degree = collections .defaultdict(set)
        for x in edges:
            degree[x[0]].add(x[1])
            degree[x[1]].add(x[0])
        while len(degree) > 2:
            cur = []
            for x in degree:
                if len(degree[x]) == 1:
                    cur.append ((degree[x].pop (),x))
            for y,x in cur:
                degree.pop(x)
                if y in degree:
                    degree[y] .discard(x)
        res = []
        for x in degree:
            res.append(x)

