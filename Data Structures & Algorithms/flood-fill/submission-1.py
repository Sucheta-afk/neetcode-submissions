class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start=image[sr][sc]

        def dfs(i, j):
            if i<0 or j<0 or i>=len(image) or j>=len(image[0]) or image[i][j]==color or image[i][j]!=start:
                return
            #elif image[i][j]==start:
            image[i][j]=color
            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i-1, j)
            dfs(i, j-1)
        
        if image[sr][sc]!=color:
            dfs(sr, sc)
        return image