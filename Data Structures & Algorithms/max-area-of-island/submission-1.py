class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxi=0
        visited=set()
        rows=len(grid)
        cols=len(grid[0])
        def dfs(r,c):
            if r>=rows or c>=cols or r<0 or c<0:
                return 0 
            if grid[r][c]==0:
                return 0
            if (r,c)  in visited:
                return 0
            visited.add((r,c))
            area=1
            area+=dfs(r+1,c)
            area+=dfs(r-1,c)
            area+=dfs(r,c+1)
            area+=dfs(r,c-1)
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visited:
                    maxi=max(maxi,dfs(r,c))
        return maxi



        