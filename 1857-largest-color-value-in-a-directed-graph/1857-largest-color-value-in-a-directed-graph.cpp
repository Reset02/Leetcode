class Solution {
public:
    int largestPathValue(string colors, vector<vector<int>>& edges) {
        int n = colors.size();
        vector<vector<int>> graph(n);
        vector<int> indegree(n, 0);

        // 建立圖與計算入度
        for (auto& edge : edges) {
            int u = edge[0], v = edge[1];
            graph[u].push_back(v);
            indegree[v]++;
        }

        // 建立 dp 陣列，dp[i][c] 表示從起點到 i，顏色 c 出現的最大次數
        vector<vector<int>> dp(n, vector<int>(26, 0));
        
        queue<int> q;
        // 將所有入度為 0 的節點放入 queue
        for (int i = 0; i < n; ++i) {
            if (indegree[i] == 0)
                q.push(i);
            dp[i][colors[i] - 'a'] = 1; // 初始化：自己的顏色出現一次
        }

        int visited = 0;
        int maxColorCount = 0;

        while (!q.empty()) {
            int node = q.front(); q.pop();
            visited++;
            maxColorCount = max(maxColorCount, *max_element(dp[node].begin(), dp[node].end()));

            for (int neighbor : graph[node]) {
                for (int c = 0; c < 26; ++c) {
                    int add = (colors[neighbor] - 'a' == c) ? 1 : 0;
                    dp[neighbor][c] = max(dp[neighbor][c], dp[node][c] + add);
                }
                indegree[neighbor]--;
                if (indegree[neighbor] == 0)
                    q.push(neighbor);
            }
        }

        // 如果還有節點沒被處理，代表圖中有環
        return visited == n ? maxColorCount : -1;
    }
};