class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        visited=[[False for _ in range(cols)] for _ in range(rows)]
        max_area=0
        def dfs(i, j):
            area=0
            if i<0 or j<0 or i>=rows or j>=cols or visited[i][j]==True or grid[i][j]==0:
                return 0
            visited[i][j]=True
            area+=1
            area+=dfs(i+1, j)
            area+=dfs(i, j+1)
            area+=dfs(i-1, j)
            area+=dfs(i, j-1)
            return area
        
        for i in range(rows):
            for j in range(cols):
                if visited[i][j]==False and grid[i][j]==1:
                    area=dfs(i, j)
                    max_area=max(max_area, area)
        return max_area
