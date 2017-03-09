# coding=utf-8
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if people == []:
            return []
        res = []
        d = collections.defaultdict (list)
        people.sort(key = lambda (x ,y): (y,x), reverse = True)
        for x in people:
            d[x[0]].append(x[1])
        temp = people[-1]
        while len(people) > 1:
            
            
            res.append((temp[0] ,d[temp[0]][-1]))
            d[temp[0]].pop()
            for x in people:
                if x[0] <= temp[0]:
                    x[1] -= 1
            #people.sort(key = lambda (x,y): (y,x), reverse = True)
            temp = min(x for x in people if x[1] == 0)
            people.remove(temp)
            #print people

