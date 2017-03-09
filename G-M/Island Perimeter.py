# coding=utf-8
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        length = len(grid)
        width = len(grid[0])
        ans = 0
        cur = set()
        #next = set()
        for i in xrange(length):
            for j in xrange(width):
                if grid[i][j] == 1:
                    ans += 4
                    
                    if j in cur:
                        ans -= 2
                    if j > 0 and grid[i][j-1] == 1:
                        ans -= 2
                    cur.add(j)
                else:
                    cur.discard(j)
                    #print i,j,ans
            #cur = copy.deepcopy(next)
            #next.clear()
            #print cur,next
        return ans
