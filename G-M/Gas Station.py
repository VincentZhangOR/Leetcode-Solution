# coding=utf-8
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas)<sum(cost):
            return -1
        n=len(gas)
        diff=0
        index=0
        for i in xrange(n):
            if gas[i]+diff<cost[i]:
                index=i+1
                diff=0
            else:
                diff+=gas[i]-cost[i]
        return index
