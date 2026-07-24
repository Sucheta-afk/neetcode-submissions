class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        visited=[[False for _ in range(cols)]for _ in range(rows)]
        #dfs funtion implementation
        #out of bounds, grid[i][j]=="0",visited[i][j]==True
        def dfs(i, j):
            if i<0 or j<0 or i>=rows or j>=cols or grid[i][j]=="0" or visited[i][j]==True:
                return
            visited[i][j]=True
            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i-1, j)
            dfs(i, j-1)
        #traversal to find land
        
        count=0
        for i in range(rows):
            for j in range(cols):
                if visited[i][j]==False and grid[i][j]=="1" :
                    count+=1
                    dfs(i, j)
        return count
