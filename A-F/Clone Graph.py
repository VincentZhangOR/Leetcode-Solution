# coding=utf-8
# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None
        d = {}
        dummy = UndirectedGraphNode (node.label)
        queue = [node]
        d[node.label] = dummy
        while len(queue) > 0:
            top = queue.pop()
            temp = d[top.label]
            temp.neighbors = []
            for x in top.neighbors:
                if x.label not in d:
                    d[x.label] = UndirectedGraphNode (x.label)
                    queue.append(x)
                temp.neighbors.append (d[x.label])
        return dummy
