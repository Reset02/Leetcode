import heapq

class Solution:
    def swimInWater(self, grid):
        n = len(grid)
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = [[False]*n for _ in range(n)]
        
        # 優先隊列 (time, x, y)
        heap = [(grid[0][0], 0, 0)]
        visited[0][0] = True
        res = 0
        
        while heap:
            time, x, y = heapq.heappop(heap)
            res = max(res, time)
            if x == n-1 and y == n-1:
                return res
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    heapq.heappush(heap, (grid[nx][ny], nx, ny))
