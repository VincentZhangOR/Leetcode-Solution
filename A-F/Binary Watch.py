# coding=utf-8
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        res = []
        for hour in xrange(4):
            min = num - hour
            if min < 0 or min > 5:
                continue
            for x in itertools .combinations(range(4 ),hour):
                temph = 0
                for a in x:
                    temph += 2**a
                if temph > 11:
                    continue
                temph = str(temph)
                for y in itertools .combinations(range (6),min):
                    tempm = 0
                    for b in y:
                        tempm += 2**b
                    if tempm > 59:
                        continue
                    tempm = str(tempm) if tempm>=10 else "0"+str(tempm)
                    temp = temph + ":" + tempm
                    res.append(temp)
        return res
        
