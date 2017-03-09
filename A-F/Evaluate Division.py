# coding=utf-8
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        res = []
        d = collections.defaultdict (lambda: collections .defaultdict(lambda: float ('inf')))
        for i in xrange(len(equations )):
                            d[equations[i][0]][equ ations[i][1]] = values[i]
                            d[equations[i][1]][equ ations[i][0]] = 1.0 / values[i]
        for k in d:
            d[k][k] = 1.0
            for u in d:
                for v in d:
                #d[u,v] = float('inf')
                #d[u,u] = 1.0
                #d[v,v] = 1.0
                    #print d[u,v]
                    d[u][v] = min (d[u][v], d[u][k] * d[k][v])
                        #d[u,v] = d[u ,k] * d[k,v]
                    #d[u,v] = min(d[u ,v], d[u,k] * d[k ,v])
        for x in queries:
            #a, b = x[0], x[1]
            if d[x[0]][x[1]] < float ('inf'):
                res.append (d[x[0]][x[1]])
            else:
                res.append(-1.0)
        return res
