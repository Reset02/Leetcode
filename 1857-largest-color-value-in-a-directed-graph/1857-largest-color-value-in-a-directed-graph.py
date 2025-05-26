class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = defaultdict(list)
        indegree = [0] * n

        # 建圖 + 入度
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        # dp[i][c]：到達節點 i，顏色 c（0~25）最多出現了幾次
        dp = [[0] * 26 for _ in range(n)]

        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        
        # 初始：每個節點的自己顏色先+1
        for i in range(n):
            color_index = ord(colors[i]) - ord('a')
            dp[i][color_index] = 1

        visited = 0
        max_color_value = 0

        while queue:
            node = queue.popleft()
            visited += 1
            for neighbor in graph[node]:
                for c in range(26):
                    dp[neighbor][c] = max(dp[neighbor][c], dp[node][c] + (1 if c == ord(colors[neighbor]) - ord('a') else 0))
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
            max_color_value = max(max_color_value, max(dp[node]))

        # 有 cycle
        return -1 if visited < n else max_color_value