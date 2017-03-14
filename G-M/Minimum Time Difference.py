class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        n = len(timePoints)
        arr = []
        for i in xrange(n):
            arr.append(self.help(timePoints[i]))
        res = float('inf')
        arr.sort(reverse = True)
        for i in xrange(n-1):
            res = min(res, arr[i] - arr[i+1])
        return min(res, arr[-1] + 24*60 - arr[0])
        
    def help(self, time):
        l = time.split(':')
        return int(l[0]) * 60 + int(l[1])