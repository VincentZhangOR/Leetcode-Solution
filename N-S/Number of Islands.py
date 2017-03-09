# coding=utf-8
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid==None or grid==[]:
            return 0
        m=len(grid)
        n=len(grid[0])
        queue=[]
        #d=set()
        i=0
        j=0
        ans=0
        while i<m and j<=n: 
            if j==n:
                i+=1
                if i==m:
                    break
                j=0
            if grid[i][j]=='1':
                queue.append((i,j))
                #d.add((i,j))
                ans+=1
                while queue!=[]:
                    frontier=[]
                    for (p,q) in queue:
                        if p and grid[p-1][q]=='1':
                            frontier .append((p-1,q))
                            grid[p -1][q]='0'
                        if p+1<m and grid[p+1][q]=='1':
                            frontier .append((p+1,q))
                            grid[p +1][q]='0'
                        if q and grid[p][q-1]=='1':
                            frontier .append((p,q-1))
                                              grid[p][q-1]='0'
                        if q+1<n and grid[p][q+1]=='1':
                            frontier .append((p,q+1))
                                              grid[p][q+1]='0'
                    queue=frontier
            j+=1
        return ans

