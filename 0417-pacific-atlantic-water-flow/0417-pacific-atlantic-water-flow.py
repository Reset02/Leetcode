class Solution:
    def pacificAtlantic(self, heights):
        if not heights or not heights[0]:
            return []

        m, n = len(heights), len(heights[0])
        pacific_reachable = set()
        atlantic_reachable = set()

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c, visited, prev_height):
            # 超出邊界或已訪問過
            if (r < 0 or c < 0 or r >= m or c >= n or
                (r, c) in visited or heights[r][c] < prev_height):
                return
            visited.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, visited, heights[r][c])

        # 太平洋邊界（上邊、左邊）
        for i in range(m):
            dfs(i, 0, pacific_reachable, heights[i][0])
        for j in range(n):
            dfs(0, j, pacific_reachable, heights[0][j])

        # 大西洋邊界（下邊、右邊）
        for i in range(m):
            dfs(i, n - 1, atlantic_reachable, heights[i][n - 1])
        for j in range(n):
            dfs(m - 1, j, atlantic_reachable, heights[m - 1][j])

        # 取交集
        result = list(pacific_reachable & atlantic_reachable)
        return result
