# coding=utf-8
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        head = collections.defaultdict (set)
        tail = collections.defaultdict (set)
        for x in prerequisites:
            head[x[1]].add(x[0])
            tail[x[0]].add(x[1])
        free = set(range(numCourses))
        for x in range(numCourses):
            if x in tail:
                free.discard(x)
        while len(free) > 0:
            cur = free.pop()
            for x in head[cur]:
                if x not in tail:
                    continue
                tail[x].discard(cur)
                if len(tail[x]) == 0:
                    free.add(x)
                    tail.pop(x)
        if len(tail) > 0:
            return False
        return True
                
                    
