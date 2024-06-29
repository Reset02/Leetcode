class Solution {
public:
    vector<vector<int>> getAncestors(int n, vector<vector<int>>& edges) {
        // Step 1: 建立圖的鄰接表表示和入度表
        vector<vector<int>> graph(n);
        vector<int> in_degree(n, 0);
        
        for (const auto& edge : edges) {
        int u = edge[0];
        int v = edge[1];
        graph[u].push_back(v);
        in_degree[v]++;
        }

        // Step 2: 拓撲排序
        vector<int> topo_order;
        queue<int> q;
        for (int i = 0; i < n; ++i) {
            if (in_degree[i] == 0) {
                q.push(i);
            }
        }

        while (!q.empty()) {
            int node = q.front();
            q.pop();
            topo_order.push_back(node);
            for (int neighbor : graph[node]) {
                in_degree[neighbor]--;
                if (in_degree[neighbor] == 0) {
                    q.push(neighbor);
                }
            }
        }

        // Step 3: 找出每個節點的所有祖先節點
        vector<set<int>> ancestors(n);
        
        for (int node : topo_order) {
            for (int neighbor : graph[node]) {
                ancestors[neighbor].insert(node);
                ancestors[neighbor].insert(ancestors[node].begin(), ancestors[node].end());
            }
        }

        // 將結果轉換為列表格式並按要求返回
        vector<vector<int>> result(n);
        for (int i = 0; i < n; ++i) {
            result[i] = vector<int>(ancestors[i].begin(), ancestors[i].end());
        }
        return result;
    }
};